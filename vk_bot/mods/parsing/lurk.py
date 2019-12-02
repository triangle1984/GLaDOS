from vk_bot.core.modules.basicplug import BasicPlug
from bs4 import BeautifulSoup
import requests


class Lurk(BasicPlug):
    command = ("лурк",)
    doc = "Поиск по лукру. Аналогично вики"

    def main(self):
        text = " ".join(self.text[1:])
        url = f"http://lurkmore.to/{text}"
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "lxml")
        error = "В настоящий момент тут ничего нет. Но вы можете:"
        try:
            result = soup.find(property="og:description")
            result = result.attrs['content'].replace(error, "нэ найдено")
            self.sendmsg(result + f"\n Ссылка на полную страницу: {url}")
        except:
            self.sendmsg("нэ найдено")
