from vk_bot.core.utils.modutil import BacisPlug
class Online(BacisPlug):
    doc = "Список онлайн участников беседы"
    command = ["/онлайн", "/online"]
    def main(self):
        onlinenumber = 0
        onlinelist = []
        onlineid = self.vk.messages.getConversationMembers(peer_id=self.event.object.peer_id)['profiles']
        for a in onlineid:
            if a['online'] == 1:
                onlinenumber+=1
                onlinelist.append(f"{str(onlinenumber)}. {a['first_name']} {a['last_name']}")
        onlinejoin = "\n".join(onlinelist)
        print(onlinejoin)
        self.sendmsg(f"Участники онлайн:\n{onlinejoin}")