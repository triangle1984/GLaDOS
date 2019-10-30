from vk_bot.core.utils.modutil import BacisPlug
import requests
from loadevn import donatetoken
from vk_bot.core.sql.vksql import tableadd
class Checkdonate(BacisPlug):
    doc = "Проверить донатил ли юзер"
    command = ["/чекнидонат"]
    def main(self):
        url = f"https://api.vkdonate.ru?action=donates&count=50&sort=sum&key={donatetoken}"
        r = requests.get(url)
        text = r.json()
        if not text["donates"]:
            self.sendmsg("ниеть, донатов от вас не было", "video-157509098_456239021")
        else:
            for donate in text["donates"]:
                if donate["uid"] == self.uid:
                    self.sendmsg(f"а вы мисье донатер. Надонатил: {donate['sum']}₽. Терь вы с випкой", "video139157356_456239665")
                    tableadd("vips", "id", self.uid, one=True)