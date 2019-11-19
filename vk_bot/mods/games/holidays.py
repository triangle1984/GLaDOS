from vk_bot.core.modules.basicplug import BasicPlug
from bs4 import BeautifulSoup
import requests
import random


class Holidays(BasicPlug):
    command = ["/праздники"]
    doc = "какие седня праздники"

    def main(self):
        req = requests.get("http://kakoysegodnyaprazdnik.ru/")
        soup = BeautifulSoup(req.text, "lxml")
        result = ["Седня празднуем: "]
        for text in soup.find_all('span', itemprop="text"):
            text = str(text)
            text = text.replace('<span itemprop="text">', "")
            text = text.replace('</span>', "")
            smile = random.choice(["🎈", "🎊", "🎉"])
            result.append(f"{smile} {text}")
        result = "\n".join(result)
        self.sendmsg(result)
