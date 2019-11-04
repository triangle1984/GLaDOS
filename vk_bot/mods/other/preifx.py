from vk_bot.core.modules.basicplug import BacisPlug
from vk_bot.core.sql.sqlgame import update
class Prefix(BacisPlug):
    command = ["/префикс", "/preifx", "/кличка", "/зовименя"]
    doc = "Сменить то, как к вам обращается бот"
    def main(self):
        response = update(self.uid, self.text)
        if response:
            self.mc2['prefix'] = response
            self.mc.set(str(self.uid), self.mc2)
            self.sendmsg("префикс успешно сменен~")
        else:
            self.sendmsg("максимальная длина префикса - 30")
