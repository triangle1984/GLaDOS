import vk_api
from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.modules.chatmager import ChatManager
from loadevn import permban
from vk_bot.core.sql.vksql import *


class Permban(BasicPlug, ChatManager):
    doc = "Пермбан"
    command = ("разбан", "unban", "разбанть")

    def main(self):
        if len(self.text) > 1:
            uid = self.returnpusuid(self.text[1])[0]
        elif self.amsg:
            uid = self.amsg["from_id"]
        else:
            self.sendmsg("каво разбанить")
            return
        tablerm(permban, "uid", uid,
                andd=f"chat_id = {self.event.chat_id}")
        self.sendmsg("разбанил")
