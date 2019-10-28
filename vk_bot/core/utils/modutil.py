from vk_api.utils import get_random_id
class BacisPlug:
    included = True
    types = ["message_new"]
    doc = "Заполните справку в модуле"
    def __init__(self, vk, vk2, upload):
        self.vk = vk
        self.vk2 = vk2
        self.upload = upload
    def givedata(self, uid, text, event, mc2, prefix, peer):
        self.uid = uid
        self.text = text
        self.event = event
        self.mc2 = mc2
        self.prefix = prefix
        self.peer_id = peer
    def sendmsg(self, msg, attachmentst=None, disable_mentions=True):
        try:
            peer_id = self.event.object.peer_id
        except:
            peer_id = self.event.peer_id
        prefix = f"*id{self.uid}({self.prefix})"
        self.vk.messages.send(peer_id=peer_id, random_id=get_random_id(),
                        message=f"{prefix}, {msg}", disable_mentions=disable_mentions,
                        attachment=attachmentst)
    def uploadphoto(self, photo):
        response = self.upload.photo_messages(photos=photo)[0]
        return f"photo{response['owner_id']}_{response['id']}"
