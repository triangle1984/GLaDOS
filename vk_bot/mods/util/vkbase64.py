from vk_bot.core.modules.basicplug import BasicPlug
import base64
class Vkbase64(BasicPlug):
    doc = "Зашифровать или расшифровать текст"
    command = ("зашифровать", "расшифровать",)
    def main(self):
        com = self.text[0].lower()
        if com == "зашифровать":
            self.sendmsg(vkbase64(self.text, encode=True))
        elif com == "расшифровать":
            self.sendmsg(vkbase64(self.text, decode=True))

def vkbase64(text, encode=False, decode=False):
    text = " ".join(text[1:])
    try:
        if encode:
            result = base64.b64encode(bytes(text, 'utf-8'))
        else:
            result = base64.b64decode(text)
    except:
        return "!error"
    return result.decode('utf-8')