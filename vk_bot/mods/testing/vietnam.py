from PIL import Image, ImageDraw
from loadevn import *
import io, requests, random, os
from vk_bot.modutil import BacisPlug
class Quote(BacisPlug):
    doc = "Фильтр Вьетнам"
    command = ["/вьетнам"]
    def main(self):
        url = self.event.object['attachments'][0]['photo']['sizes'][-1]['url']
        img = requests.get(url).content
        f = io.BytesIO(img)
        image = Image.open(f)
        vietnam = Image.open('/usr/local/bin/danila/vk-bot/vk_bot/mods/testing/u-s-_helicopters_vietnam.jpg')
        (width, height) = image.size
        resized_img = vietnam.resize((width, height), Image.ANTIALIAS)
        image.paste(resized_img.convert('RGB'), (0, 0), resized_img)
        name = f"name{random.randint(0, 1000)}.jpg"
        image.save(name)
        try:
            attachment  = self.uploadphoto(name)
            self.sendmsg("Дэржите фотку", attachment)
        finally:
            os.remove(name)
