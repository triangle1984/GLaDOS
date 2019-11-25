from PIL import Image, ImageDraw
import requests, random, io
from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.modules.upload import Upload


class Quote(BasicPlug, Upload):
    doc = "Фильтр кек"
    command = ["/кек"]

    def main(self):
        url = self.event.object['attachments'][0]['photo']['sizes'][-1]['url']
        img = requests.get(url).content
        f = io.BytesIO(img)
        image = Image.open(f)
        width, height = image.size
        if not width%2 == 0:
            width-=1
        kek = Image.new("RGB", (width, height))
        wid = round(int(width / 2))
        img = image.crop((0, 0, wid, height))
        mirror = img.transpose(Image.FLIP_LEFT_RIGHT)
        kek.paste(img, (0,0), img.convert('RGBA'))
        kek.paste(mirror, (int(wid), 0), mirror.convert('RGBA'))
        name = f"name{random.randint(0, 1000)}.jpg"
        kek.save(name)
        attachment = self.uploadphoto(name)
        self.sendmsg("Дэржите фотку", attachment)