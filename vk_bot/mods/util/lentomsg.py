from vk_bot.core.modules.basicplug import BasicPlug
class Lentomsg(BasicPlug):
    doc = "Длина сообщения"
    command = ("длина",)
    def main(self):
        text = " ".join(self.text[1:])
        length = len(text)
        self.sendmsg(f"Символов в сообщении: {length}")