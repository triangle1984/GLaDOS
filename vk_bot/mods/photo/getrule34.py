from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.modules.othermethods import OtherMethod
import requests, random
class GetRule34(BasicPlug, OtherMethod):
    doc = "Скора ето буит руле34"
    command = ["/руле34"]
    def main(self):
        url = "https://r34-json-api.herokuapp.com/posts"
        params = {
            "tags": self.text[1:],
            "limit": 50
        }
        r = requests.get(url, params=params).json()
        r = random.choice(r)['file_url']
        photos = self.dowloadupload(r)
        self.sendmsg("Тест", photos)
