from vk_bot.core.modules.basicplug import BasicPlug
import requests
from datetime import timedelta
class Anime(BasicPlug):
    doc = "Распознать аниме на фото"
    command = ["/анименафото"]
    def main(self):
        try:
            image_url = self.event.object['attachments'][0]['photo']['sizes'][-1]['url']
            api = f'https://trace.moe/api/search'
            params = {
                'url': image_url
            }
            r = requests.get(api, params=params)
            encode = r.json()
            name = encode["docs"][0]["title_english"]
            episode = encode["docs"][0]["episode"]
            chance = round(encode['docs'][0]["similarity"] * 100)
            sec = round(encode["docs"][0]["from"])
            time = timedelta(seconds = sec)
            self.sendmsg(f"""Я думаю это: {name}
            Серия: {episode}
            Точность: {chance}%
            Тайминг: {time}""")
        except IndexError:
            self.sendmsg("Мне нужно фото!")
