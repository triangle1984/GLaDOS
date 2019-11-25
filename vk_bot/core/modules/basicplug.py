class BasicPlug:
    included = True
    attachment = False
    action = False
    thread = False
    types = 'command'
    vktypes = ["message_new"]
    uberequests = [False]
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
        # self.peer_id = peer
        self.mc = mc

    def makeothervariables(self):
        try:
            self.peer_id = self.event.object.peer_id
        except:
            self.peer_id = self.event.peer_id
        try:
            self.fwd_messages = self.event.object.fwd_messages
            self.reply_message = self.event.object.reply_message
            # страничный бот, я тебя ненавижу
        except:
            return
        if self.fwd_messages:
            self.amsg = self.fwd_messages[0]
        else:
            self.amsg = self.reply_message

    def sendmsg(self, msg, attachmentst=None, disable_mentions=True, prefix=True, peer_id=False):
        if peer_id == False:
            peer_id = self.peer_id
        if prefix:
            prefix = f"*id{self.uid}({self.mc2['prefix']}), "
        else:
            prefix = ""
        self.vk.messages.send(peer_id=peer_id, random_id=0,
                              message=f"{prefix}{msg}", disable_mentions=disable_mentions,
                              attachment=attachmentst)

    def returnpusuid(self, text):
        text = text.replace("[", "").replace("]", "").split("|")
        text[0] = text[0].replace("club", "-")
        text[0] = text[0].replace("id", "")
        return text
