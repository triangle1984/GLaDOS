import vk_api
from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.modules.chatmager import ChatManager
from vk_bot.core.modules.othermethods import OtherMethod


class Kick(BasicPlug, ChatManager, OtherMethod):
    doc = "Кик юзера"
    command = ["/кик"]

    def main(self):
        if len(self.text) > 1:
            uid = self.returnpusuid(self.text[1])[0]
        elif self.amsg:
            uid = self.amsg["from_id"]
        else:
            self.sendmsg("каво кикать")
            return
        uadmin = self.checkuadmin()
        if uadmin:
            try:
                self.vk.messages.removeChatUser(
                    chat_id=self.event.chat_id, user_id=uid)
            except vk_api.exceptions.ApiError:
                self.sendmsg("Нэ удалось  кикнуть")
        else:
            self.sendmsg("Вы нэ админ беседы")
