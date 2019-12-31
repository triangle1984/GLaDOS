import vk_api
from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.modules.chatmager import ChatManager
from vk_bot.config import permban
from vk_bot.core.sql.vksql import *


class Permban(BasicPlug, ChatManager):
    doc = "Пермбан"
    command = ("пермбан", "permban", "бан")
    included = False

    def main(self):
        if len(self.text) > 1:
            uid = self.returnpusuid(self.text[1])[0]
        elif self.amsg:
            uid = self.amsg["from_id"]
        else:
            self.sendmsg("каво кикать")
            return
        self.kick(uid)
        if not checktable(f"{permban}", "chat_id", f"{self.event.chat_id}", andd=f"uid = {uid}"):
            tableadd(f'{permban}', "uid, chat_id",
                     f"{uid}, {self.event.chat_id}")
        self.sendmsg("забанен нахой")
