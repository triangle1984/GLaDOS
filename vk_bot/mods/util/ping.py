from vk_bot.core.utils.modutil import BacisPlug
class Ping(BacisPlug):
    doc = "Проверить, жив ли бот"
    command = ["/жив?"]
    def main(self):
        self.sendmsg("JA JA Führer")