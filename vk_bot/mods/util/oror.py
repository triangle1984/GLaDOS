from vk_bot.core.modules.basicplug import BasicPlug
import random
class Oror(BasicPlug):
    doc = "Выбрать что-либо из предложенных вариантов"
    command = ["/выбери"]
    def main(self):
        text = " ".join(self.text[1:])
        text = random.choice(text.split("или"))
        self.sendmsg(f"я выбираю: {text}")