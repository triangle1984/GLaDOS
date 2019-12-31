from PIL import Image, ImageDraw
from vk_bot.config import *
import io, requests, random, os
from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.modules.upload import Upload
class Bob(BasicPlug, Upload):
    doc = "вашу пикчу нарисует сам Боб Росс!"
    command = ("боб",)
    def main(self):
        url = self.event.object['attachments'][0]['photo']['sizes'][-1]['url']
        img = requests.get(url).content
        f = io.BytesIO(img)
        image = Image.open(f)
        resized_img = image.resize((448, 447), Image.ANTIALIAS)
        bob = Image.open('pics/bob.png')
        resized_img = resized_img.convert('RGBA')
        paint = Image.open('pics/e2e46dbe6f89b13bcdcfaafa883753f9.jpg')
        paint.paste(resized_img, (109, 40), resized_img)
        paint.paste(bob, (0, 0), bob)
        name = f"name{random.randint(0, 1000)}.png"
        paint.save(name)
        try:
            attachment  = self.uploadphoto(name)
            self.sendmsg("Дэржите фотку", attachment)
        finally:
            os.remove(name)