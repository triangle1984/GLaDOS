from vk_api.utils import get_random_id
class BacisPlug:
    included = True
    types = ["message_new"]
    doc = "Заполните справку в модуле"
    def __init__(self, vk, vk2):
        self.vk = vk
        self.vk2 = vk2
    def givedata(self, uid, text, event, mc2, prefix, peer):
        self.uid = uid
        self.text = text
        self.event = event
        self.mc2 = mc2
        self.prefix = prefix
        self.peer_id = peer
    def sendmsg(self, msg, attachmentst=None):
        try:
            peer_id = self.event.object.peer_id
        except:
            print(".")
            peer_id = self.event.peer_id
        self.vk.messages.send(peer_id=peer_id, random_id=get_random_id(),
                        message=f"{self.prefix}, {msg}",
                        attachment=attachmentst)

