from vk_api.utils import get_random_id


class BasicPlug:
    included = True
    attachment = False
    types = 'command'
    vktypes = ["message_new"]
    doc = "Заполните справку в модуле"
    available_for = "user"

    def __init__(self, vk, vk2, upload):
        self.vk = vk
        self.vk2 = vk2
        self.upload = upload

    def givedata(self, uid, text, event, mc2, prefix, peer, mc):
        self.uid = uid
        self.text = text
        self.event = event
        self.mc2 = mc2
        self.prefix = prefix
        self.peer_id = peer
        self.mc = mc

    def sendmsg(self, msg, attachmentst=None, disable_mentions=True):
        try:
            peer_id = self.event.object.peer_id
        except:
            peer_id = self.event.peer_id
        prefix = f"*id{self.uid}({self.mc2['prefix']})"
        self.vk.messages.send(peer_id=peer_id, random_id=get_random_id(),
                              message=f"{prefix}, {msg}", disable_mentions=disable_mentions,
                              attachment=attachmentst)
