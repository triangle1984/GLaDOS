from PIL import Image, ImageDraw
from vk_bot.config import *
import io, requests, random, os
from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.modules.upload import Upload
class Tnn(BasicPlug, Upload):
    doc = "ТЯН НЕ НУЖНЫ"
    command = ("тнн",)
    def main(self):
        url = self.event.object['attachments'][0]['photo']['sizes'][-1]['url']
        img = requests.get(url).content
        f = io.BytesIO(img)
        image = Image.open(f)
        resized_img = image.resize((159, 95), Image.ANTIALIAS)
        resized_img = resized_img.convert('RGBA')
        resized_img = resized_img.rotate(-2)
        tnn = Image.open('pics/test.png')
        tnn.paste(resized_img, (403, 103), resized_img)
        name = f"name{random.randint(0, 1000)}.png"
        tnn.save(name)
        try:
            attachment  = self.uploadphoto(name)
            self.sendmsg("Дэржите фотку", attachment)
        finally:
            os.remove(name)
