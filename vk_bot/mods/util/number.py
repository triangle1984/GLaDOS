from vk_bot.core.utils.modutil import BacisPlug
import random
class Number(BacisPlug):
    doc = "Рандомное число из заданного диапазона"
    command = ["/число"]
    def main(self):
        try:
            x = int(self.text[1])
            y = int(self.text[2])
            nubmer2 = random.randint(x, y)
        except:
            return
        self.sendmsg(f"Число: {nubmer2}")