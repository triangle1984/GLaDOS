from vk_bot.core.modules.basicplug import BasicPlug
import requests
from loadevn import donatetoken
from vk_bot.core.sql.vksql import tableadd


class Checkdonate(BasicPlug):
    doc = "Проверить донатил ли юзер"
    command = ("чекнидонат",)

    def main(self):
        url = f"https://api.vkdonate.ru?action=donates&count=50&sort=sum&key={donatetoken}"
        r = requests.get(url)
        text = r.json()
        msg = "ниеть, донатов от вас не было"
        attachments = '157509098_456239021'
        udonate = False
        for donate in text['donates']:
            if donate["uid"] == self.uid:
                udonate += donate['sum']
        if udonate:
            tableadd("vips", "id", self.uid, one=True)
            self.sendmsg(
                f"а вы мисье донатер. Надонатил: {udonate}₽. Терь вы с випкой",
                "video139157356_456239665")
        else:
            self.sendmsg("Ниеть, донатов от вас не было",
                         'video157509098_456239021')
