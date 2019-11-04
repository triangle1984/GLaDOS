from vk_bot.core.modules.basicplug import BasicPlug
import random
class Chance(BasicPlug):
    doc = "Вероятность какого-либо события"
    command = ["/шансы", "/вероятность"]
    def main(self):
        text = " ".join(self.text[1:])
        rnd =  random.randint(0, 100)
        message = f"Вероятность {text} равна {rnd}%"
        self.sendmsg(message)