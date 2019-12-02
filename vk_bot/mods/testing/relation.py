from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.sql.vksql import *
import pylibmc
class Relation(BasicPlug):
    doc = "Отношения"
    command = ("отношения",)
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
            tableadd('relation', "id, id2", f'{uid}, {uid2}')
            self.mc.delete(f"r{self.uid}")
        else:
            self.sendmsg("запросов не поступало")
    def deny(self):
        self.mc.delete(f"r{self.uid}")     
        if self.mc.delete(f"r{self.uid}") == False:
            self.sendmsg("запросов не поступало")
    def offer(self):
        uid2 = self.returnpusuid(self.text[2][3:])[0]
        if self.mc.get(f"r{uid2}"):
            self.sendmsg("вы уже отправили запрос")
        if checktable("relation", "id2 or id", self.uid):
            self.sendmsg("ты уже встречаешься")
        else: 
            self.mc.set(f"r{uid2}", self.uid, time=120)
    def statrelation(self):
        if not checktable("relation", "id2 or id", self.uid):
            self.sendmsg("ни с кем не встречаешься")
        else:
            user = checktable("relation", "id2 or id", self.uid)
            if user['id'] == self.uid:
                user = user['id2']
            else:
                user = user['id']
            nameid = f"*id{user}({self. vk.users.get(user_ids=user, name_case='ins')[0]['first_name']})"    
            self.sendmsg(f"Ты встречаешься с {nameid}")