from vk_bot.core.utils.modutil import BacisPlug
import random
class Oror(BacisPlug):
    doc = "Выбрать что-либо из предложенных вариантов"
    command = ["/выбери"]
    def main(self):
        text = " ".join(self.text[1:])
        text = random.choice(text.split("или"))
        self.sendmsg(f"я выбираю: {text}")