from vk_bot.core.modules.basicplug import BasicPlug
from vk_api.utils import get_random_id
from vk_bot.core.sql.vksql import *
class OnOffAgitation(BasicPlug):
    doc = "Включить или выключить рассылку в беседе"
    command = ("рассылка",)
    def main(self):
        if self.text[1] == 'выключить':
            status = '1'
            msg = "Выключено!"
        elif self.text[1] == 'включить':
            status = '0'
            msg = "Включено"  
        if checktable('mailing', "id", f"{self.event.chat_id}"):  
            tableupdate('mailing', "whitelist", f"{status}", f"id = {self.event.chat_id}") 
        else: 
            tableadd('mailing', "id, whitelist", f"{self.event.chat_id}, {status}")
        self.sendmsg(msg)    
