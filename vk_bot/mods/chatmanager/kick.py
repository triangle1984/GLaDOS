import vk_api
from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.modules.upload import Upload


class Kick(BasicPlug, Upload):
    doc = "Кик юзера"
    command = ["/кик"]

    def main(self):
        try:
            uid = self.amsg["from_id"]
        except:
            self.sendmsg("каво кикать")
            return
        uadmin = False
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
