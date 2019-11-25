from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.modules.othermethods import OtherMethod
import random
class Who(BasicPlug, OtherMethod):
    doc = "Выбирает рандомного участника беседы под вашим предлогом"
    command = ("кто",)
    def main(self):
        try:
            whotext = ' '.join(self.text[1:])
            self.sendmsg(f"Кто {whotext}? Я думаю, это {self.randomuser()}")
        except:
            self.sendmsg("Для работы этой команды боту нужна админка в беседе!")