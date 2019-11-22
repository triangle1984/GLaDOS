from vk_bot.core.modules.basicplug import BasicPlug
from vk_api.utils import get_random_id
from loadevn import speechtotext
from vk_bot.core.sql.vksql import *
class OnOff(BasicPlug):
    doc = "Включить или выключить перевод гс в беседе"
    command = ["/гс"]
    def main(self):
        if self.text[1] == 'выключить':
            status = '0'
            msg = "Выключено!"
        elif self.text[1] == 'включить':
            status = '1'
            msg = "Включено"
        if checktable(f'{speechtotext}', "chat_id", f"{self.event.object.peer_id}"):
            tableupdate(f'{speechtotext}', "status", f"{status}", f"chat_id = {self.event.object.peer_id}") 
        else:
            tableadd(f'{speechtotext}', "chat_id, status", f"{self.event.object.peer_id}, {status}")
        self.sendmsg(msg)    
