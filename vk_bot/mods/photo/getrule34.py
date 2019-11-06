from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.modules.othermethods import OtherMethod
import requests, random
class GetRule34(BasicPlug, OtherMethod):
    doc = "Скора ето буит руле34"
    command = ["/руле34"]
    available_for = "vips"
    def main(self):
        url = "https://r34-json-api.herokuapp.com/posts"
        params = {
            "tags": "+".join(self.text[1:]),
            "limit": 200
        }
        try:
            r = requests.get(url, params=params).json()
            r = random.choice(r)
            file_url = r['file_url']
            tags = ", ".join(r['tags'])
            photos = self.dowloadupload(file_url)
        except:
            self.sendmsg("Нинашол или другие причины");return
        self.sendmsg(f"Теги: {tags}", photos)
