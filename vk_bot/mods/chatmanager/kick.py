import vk_api
import requests
from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.modules.upload import Upload


class Kick(BasicPlug, Upload):
    doc = "Кик юзера"
    command = ["/кик"]

    def main(self):
        if not self.event.object.fwd_messages:
            self.msg = self.event.object.reply_message
        else:
            self.msg = self.event.object.fwd_messages[0]
        uid = self.msg["from_id"]
        for a in self.vk.messages.getConversationMembers(peer_id=self.event.object.peer_id)['items']:
            try:
                if a['member_id'] == self.event.object.from_id:
                    if 'is_admin' in a:
                        self.vk.messages.removeChatUser(chat_id=self.event.chat_id, user_id=uid)
                    else:
                        self.sendmsg("Вы не админ беседы!")
            except:
                self.sendmsg("ОШИБКА НАХУЙ")