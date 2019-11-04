from vk_bot.core.modules.basicplug import BacisPlug
import time
class Counting(BacisPlug):
    command = ["/отсчет"]
    doc = "Отсчет от 1 до 3"
    def main(self):
        for x in range(3, -1, -1):
            if x == 0:
                return
            self.sendmsg(x)
            time.sleep(1)
