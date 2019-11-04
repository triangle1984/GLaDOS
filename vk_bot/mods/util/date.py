from vk_bot.core.modules.basicplug import BacisPlug
import random
class Date(BacisPlug):
    doc = "Дата какого-либо события"
    command = ["/дата"]
    def main(self):
        text = " ".join(self.text[1:])
        day = random.randint(1,31)
        moth = random.randint(1,12)
        year = random.randint(2019, 2100)
        when = year-2019
        event = f"Дата {text}: {day}.{moth}.{year}, через {when} лет"
        self.sendmsg(event)