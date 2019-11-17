import vk_api
from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.modules.upload import Upload
from vk_bot.core.modules.othermethods import OtherMethod


class Kick(BasicPlug, Upload, OtherMethod):
    doc = "Кик юзера"
    command = ["/кик"]

    def main(self):
        if len(self.text) > 0:
            uid = self.returnpusuid(self.text[1])[0]
        elif self.amsg:
            uid = self.amsg["from_id"]
        else:
            self.sendmsg("каво кикать")
            return
        uadmin = False
        print(uid)
        for a in self.vk.messages.getConversationMembers(peer_id=self.event.object.peer_id,
                                                         fields="admins")['items']:
            if a['member_id'] == self.event.object.from_id and 'is_admin' in a:
                uadmin = True
        if uadmin:
            try:
                self.vk.messages.removeChatUser(
                    chat_id=self.event.chat_id, user_id=uid)
            except vk_api.exceptions.ApiError:
                self.sendmsg("Нэ удалось  кикнуть")
        else:
            self.sendmsg("Вы нэ админ беседы")
