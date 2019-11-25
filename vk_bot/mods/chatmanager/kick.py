import vk_api
from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.modules.chatmager import ChatManager


class Kick(BasicPlug, ChatManager):
    doc = "Кик юзера"
    command = ("кик",)

    def main(self):
        if len(self.text) > 1:
            uid = self.returnpusuid(self.text[1])[0]
        elif self.amsg:
            uid = self.amsg["from_id"]
        else:
            self.sendmsg("каво кикать")
            return
        self.kick(uid)
