from vk_bot.core.modules.basicplug import BasicPlug
from bs4 import BeautifulSoup
import requests


class Holidays(BasicPlug):
    command = ["/праздники"]
    doc = "какие седня праздники"

    def main(self):
        req = requests.get("http://kakoysegodnyaprazdnik.ru/")
        soup = BeautifulSoup(req.text, "lxml")
        for text in soup.find_all('span', itemprop="text"):
            text = str(text)
            text = text.replace('<span itemprop="text">', "")
            text = text.replace('</span>', "")
            result.append(text)
        result = "\n".join(result)
        self.sendmsg(result)
