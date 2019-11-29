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

    def __init__(self, vk, vk2, upload, uid, text, event, mc2, prefix, peer, mc, rtext):
        self.vk = vk
        self.vk2 = vk2
        self.upload = upload
        self.uid = uid
        self.text = text
        self.event = event
        self.mc2 = mc2
        self.peer_id = peer
        self.prefix = prefix
        self.mc = mc
        self.rawtext = rtext

    def makeothervariables(self):
        self.fwd_messages = self.event.object.fwd_messages
        self.reply_message = self.event.object.reply_message
        try:
            self.textnocommand = self.rawtext[self.rawtext.index(" ")+1:]
        except ValueError:
            pass
        if self.fwd_messages:
            self.amsg = self.fwd_messages[0]
        else:
            self.amsg = self.reply_message

    def sendmsg(self, msg, attachmentst=None, disable_mentions=True, prefix=True, peer_id=False, split=","):
        if peer_id == False:
            peer_id = self.peer_id
        if prefix:
            prefix = f"*id{self.uid}({self.mc2['prefix']}){split} "
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
