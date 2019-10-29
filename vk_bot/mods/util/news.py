from vk_bot.core.utils.modutil import BacisPlug
import random, requests
from loadevn import apinews
class News(BacisPlug):
    doc = "Последние новости"
    command = ["/новость"]
    def main(self):
        api = 'https://newsapi.org/v2/top-headlines'
        params = {
                    'apiKey': apinews,
                    'country': 'ru'
                    }
        r = requests.get(api, params=params, timeout=5)
        encode = r.json()
        newsjson = random.choice(encode['articles'])
        self.sendmsg(f"{newsjson['title']}\n\n{newsjson['description']}\n\nПолную статью вы можете прочитать здесь: {newsjson['url']}")