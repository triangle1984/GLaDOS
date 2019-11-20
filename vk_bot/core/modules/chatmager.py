class ChatManager:
    def checkuadmin(self):
        respon = self.vk.messages.getConversationMembers(peer_id=self.peer_id,
                                                         fields="admins")['items']
        for a in respon:
            if a['member_id'] == self.uid and 'is_admin' in a:
                return True
            return False
