from PIL import Image, ImageDraw, ImageFont
from loadevn import *
import textwrap
import io
import requests
from vk_bot.modutil import BacisPlug
class Quote(BacisPlug):
    doc = "Сделать цитату по пересланному сообщению"
    command = ["/цитата"]
    def main(self):
        astr = self.event.object.reply_message['text']
        para = textwrap.wrap(astr, width=30)
        MAX_W, MAX_H = 700, 400
        im = Image.new('RGB', (MAX_W, MAX_H), (0, 0, 0, 0))
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype('/usr/share/fonts/TTF/DejaVuSansCode-Bold.ttf',20)
        fontu = ImageFont.truetype('/usr/share/fonts/TTF/DejaVuSansCode-Bold.ttf',18)
        current_h, pad = 150, 10
        for line in para:
            w, h = draw.textsize(line, font=font)
            draw.text((250, current_h), line, font=font)
            current_h += h + pad
        url = self.vk.users.get(user_ids=self.event.object.reply_message['from_id'], fields='photo_max')[0]['photo_max']
        img = requests.get(url).content
        f = io.BytesIO(img)

        watermark = Image.open(f).convert("RGBA")
        im.paste(watermark, (10, 100),  watermark)
        firstname = self.vk.users.get(user_ids=self.event.object.reply_message['from_id'])[0]['first_name']
        lastname =  self.vk.users.get(user_ids=self.event.object.reply_message['from_id'])[0]['last_name']
        draw.text((30, 310), f'{firstname} {lastname}', font=fontu)
        im.save('test.jpg')
        print(".")
