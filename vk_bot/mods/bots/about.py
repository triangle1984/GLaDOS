from vk_bot.core.utils.modutil import BacisPlug
from vk_bot import mods
from boltons import iterutils
class AboutBot(BacisPlug):
    doc = "Инфа о боте"
    command = ["/оботе"]
    def main(self):
        info = """
        бот написан на python, двумя прогерами
        первый прогер: *slava_a_i_r
        второй прогер: *pythonoglot
        модуль на распознавание гс написал: *feelan03
        Приятного пользования~
        """
        self.sendmsg(info)