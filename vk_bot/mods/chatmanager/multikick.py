import vk_api
from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.modules.chatmager import ChatManager
from vk_bot.core.modules.othermethods import OtherMethod


class Kick(BasicPlug, ChatManager, OtherMethod):
    doc = "Кик нескольких юзеров"
    command = ["/мультикик"]

    def main(self):
        uidlist = []
        if len(self.text) > 1:
            for a in self.text[1:]:
                uid = self.returnpusuid(a)[0]
                uidlist.append(uid)
        else:
            self.sendmsg("каво кикать")
            return
        uadmin = self.checkuadmin()
        if uadmin:
            try:
                for user in uidlist:
                    self.vk.messages.removeChatUser(
                        chat_id=self.event.chat_id, user_id=user)
            except vk_api.exceptions.ApiError:
                self.sendmsg("Нэ удалось  кикнуть")
        else:
            self.sendmsg("Вы нэ админ беседы")    
