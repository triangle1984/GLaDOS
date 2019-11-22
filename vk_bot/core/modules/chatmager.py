class ChatManager:
    def checkuadmin(self):
        respon = self.vk.messages.getConversationMembers(peer_id=self.peer_id,
                                                         fields="admins")['items']
        for a in respon:
            if a['member_id'] == self.uid and 'is_admin' in a:
                return True
            return False
    def kick(self, user):
        uadmin = self.checkuadmin()
        if uadmin:
            try:
                self.vk.messages.removeChatUser(chat_id=self.event.chat_id, user_id=user)
            except vk_api.exceptions.ApiError:
                self.sendmsg("Нэ удалось  кикнуть")
        else:
            self.sendmsg("Вы нэ админ беседы")         