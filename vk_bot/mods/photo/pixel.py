from PIL import Image, ImageDraw
from vk_bot.config import *
import io, requests, random, os
from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.modules.upload import Upload
class Pixel(BasicPlug, Upload):
    doc = "Фильтр пиксель"
    command = ("пиксель",)
    def pixelate(self, image, pixel_size=9, draw_margin=True):
        margin_color = (0, 0, 0)

        image = image.resize((image.size[0] // pixel_size, image.size[1] // pixel_size), Image.NEAREST)
        image = image.resize((image.size[0] * pixel_size, image.size[1] * pixel_size), Image.NEAREST)
        pixel = image.load()

        if draw_margin:
            for i in range(0, image.size[0], pixel_size):
                for j in range(0, image.size[1], pixel_size):
                    for r in range(pixel_size):
                        pixel[i+r, j] = margin_color
                        pixel[i, j+r] = margin_color

        return image
    def main(self):
        try:
            url = self.event.object['attachments'][0]['photo']['sizes'][-1]['url']
            img = requests.get(url).content
            f = io.BytesIO(img)
            image = Image.open(f)
            image_pixelate = self.pixelate(image)
            name = f"name{random.randint(0, 1000)}.jpg"
            image_pixelate.save(name)
            attachment  = self.uploadphoto(name)
            self.sendmsg("Дэржите фотку", attachment)
        except:
            self.sendmsg("Прикрепите фото!")
            return
        finally:
            os.remove(name)