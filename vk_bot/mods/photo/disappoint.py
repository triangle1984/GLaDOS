from PIL import Image, ImageDraw
from loadevn import *
import io, requests, random, os
from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.modules.upload import Upload
class Disappoint(BasicPlug, Upload):
    doc = "Наклеивает \"огорчило\""
    command = ("огорчило",)
    def main(self):
        try:
            url = self.event.object['attachments'][0]['photo']['sizes'][-1]['url']
            img = requests.get(url).content
            f = io.BytesIO(img)
            image = Image.open(f)
            resized_img = image.resize((1080, 720), Image.ANTIALIAS)
            disappoint = Image.open('pics/1512680346_5734a2a99f15d154a59b66b4.png')
            resized_img.paste(disappoint.convert('RGB'), (220, 400), disappoint)
            name = f"name{random.randint(0, 1000)}.jpg"
            resized_img.save(name)
            attachment  = self.uploadphoto(name)
            self.sendmsg("Дэржите фотку", attachment)
        except:
            self.sendmsg("пикчонку забыли")
            return
        finally:
            os.remove(name)
