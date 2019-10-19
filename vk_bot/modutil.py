class BacisPlug:
    included = True
    types = "msg"
    doc = "Заполните справку в модуле"
    def __init__(self, vk, vk2):
        self.vk = vk
        self.vk2 = vk2
    def givedata(self, uid, text, event, mc2):
        self.uid = uid
        self.text = text
        self.event = event
        self.mc2 = mc2
