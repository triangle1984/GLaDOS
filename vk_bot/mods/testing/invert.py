from PIL import Image, ImageDraw
from loadevn import *
import io, requests, random, os
from vk_bot.modutil import BacisPlug
class Quote(BacisPlug):
    doc = "ЧНегатив фильтр"
    command = ["/негатив"]
    def main(self):
        url = self.event.object['attachments'][0]['photo']['sizes'][-1]['url']
        img = requests.get(url).content
        f = io.BytesIO(img)
        image = Image.open(f)
        draw = ImageDraw.Draw(image)
        pix = image.load() 
        (width, height) = image.size
        for i in range(width):
            for j in range(height):
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                draw.point((i, j), (255 - a, 255 - b, 255 - c))
        name = f"name{random.randint(0, 1000)}.jpg"
        image.save(name)
        try:
            attachment  = self.uploadphoto(name)
            self.sendmsg("Дэржите фотку", attachment)
        finally:
            os.remove(name)
