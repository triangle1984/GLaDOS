from vk_bot.core.modules.basicplug import BasicPlug 
from vk_bot.core.modules.othermethods import OtherMethod 
import random, vk_api 
class Pair(BasicPlug, OtherMethod): 
    doc = "Шипперит двух участников беседы" 
    command = ("шип",) 
    def main(self): 
        try: 
            person1 = self.randomuser() 
            person2 = self.randomuser() 
            while person1 == person2: 
                person2 = self.randomuser() 
            self.sendmsg(f"{person1} ❤❤❤ {person2}") 
        except vk_api.exceptions.ApiError: 
            self.sendmsg("Для работы этой команды боту нужна админка в беседе!")