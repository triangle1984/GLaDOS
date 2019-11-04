from vk_bot.core.modules.basicplug import BacisPlug
import random
class Doulikethis(BacisPlug):
    doc = "Оценка чего либо"
    command = ["/оцени"]
    def main(self):
        osenka = random.randint(0, 10)
        text = " ".join(self.text[1:])
        self.sendmsg(f"Моя оценка на {text}: {osenka}/10")