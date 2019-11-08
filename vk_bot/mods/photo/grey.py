from PIL import Image, ImageDraw
from loadevn import *
import io
import requests
import random
import os
from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.modules.upload import Upload


class Quote(BasicPlug, Upload):
    doc = "Черно-белый фильтр"
    command = ["/чб"]

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
                S = (a + b + c) // 3
                draw.point((i, j), (S, S, S))
        name = f"name{random.randint(0, 1000)}.jpg"
        image.save(name)
        try:
            attachment = self.uploadphoto(name)
            self.sendmsg("Дэржите фотку", attachment)
        finally:
            os.remove(name)
