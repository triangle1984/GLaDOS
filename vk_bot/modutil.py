from vk_api.utils import get_random_id
class BacisPlug:
    included = True
    types = "msg"
    doc = "Заполните справку в модуле"
    def __init__(self, vk, vk2):
        self.vk = vk
        self.vk2 = vk2
    def givedata(self, uid, text, event, mc2, prefix):
        self.uid = uid
        self.text = text
        self.event = event
        self.mc2 = mc2
        self.prefix = prefix
    def sendmsg(self, response):
        if "attachment" not in response:
            response["attachment"] = None
        self.vk.messages.send(peer_id=self.event.object.peer_id, random_id=get_random_id(),
                        message=f"{self.prefix}, {response['message']}",
                        attachment=response["attachment"])

