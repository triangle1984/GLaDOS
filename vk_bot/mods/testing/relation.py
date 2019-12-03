from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.sql.vksql import *
import pylibmc


class Relation(BasicPlug):
    doc = "Отношения"
    command = ("отношения2",)

    def main(self):
        try:
            requests = self.text[1]
            if requests == "встречаться":
                self.offer()
            elif requests == "принять":
                self.accept()
            elif requests == 'отказать':
                self.deny()
            elif requests == "стат":
                self.statrelation()
        except:
            pass

    def accept(self):
        uid2 = self.mc.get(f"r{self.uid}")
        uid = self.uid
        if uid2:
            self.sendmsg("ты принял предложение!")
            tableadd('relation', "id, id2", f'{uid}, {uid2}')
            self.mc.delete(f"r{self.uid}")
        else:
            self.sendmsg("запросов не поступало")
            return

    def deny(self):
        msg = "ты отклонил предложение"
        if self.mc.delete(f"r{self.uid}") == False:
            msg = "запросов не поступало"
        self.mc.delete(f"r{self.uid}")
        self.sendmsg(msg)

    def offer(self):
        uid2 = self.returnpusuid(self.text[2][3:])[0]
        if int(uid2) == self.uid:
            self.sendmsg("низя отправить предложение самому себе")
            return
        if self.mc.get(f"r{uid2}"):
            self.sendmsg("вы уже отправили запрос")
            return
        elif checktable("relation", "id2 or id", self.uid):
            self.sendmsg("ты уже встречаешься")
            return
        else:
            self.mc.set(f"r{uid2}", self.uid, time=120)
            nameid = f"*id{uid2}({self. vk.users.get(user_ids=uid2, name_case='dat')[0]['first_name']})"
            self.sendmsg(f"Ты предложил встречаться {nameid}")

    def statrelation(self):
        if not checktable("relation", "id2 or id", self.uid):
            self.sendmsg("ни с кем не встречаешься")
            return
        else:
            user = checktable("relation", "id2 or id", self.uid)
            if user['id'] == self.uid:
                user = user['id2']
            else:
                user = user['id']
            nameid = f"*id{user}({self. vk.users.get(user_ids=user, name_case='ins')[0]['first_name']})"
            self.sendmsg(f"Ты встречаешься с {nameid}")
