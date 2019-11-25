from vk_bot.core.modules.basicplug import BasicPlug
class Repeat(BasicPlug):
    doc = "Повторить сообщение"
    command = ("повтори",)
    def main(self):
        text = " ".join(self.text[1:])
        self.sendmsg(text)