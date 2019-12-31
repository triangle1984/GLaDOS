from vk_bot.core.modules.basicplug import BasicPlug
import random, requests
from vk_bot.config import apinews
class News(BasicPlug):
    doc = "Последние новости"
    command = ("новость",)
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