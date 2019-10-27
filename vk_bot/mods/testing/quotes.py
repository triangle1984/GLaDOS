from PIL import Image, ImageDraw, ImageFont
from loadevn import *
import textwrap, io, requests, random, os, datetime
from vk_bot.modutil import BacisPlug
class Quote(BacisPlug):
    doc = "Сделать цитату по пересланному сообщению"
    command = ["/цитата", "/цитаты"]
    def main(self):
        try:
            if not self.event.object.fwd_messages:
                msg = self.event.object.reply_message
                astr = msg['text']
            else:
                msg = self.event.object.fwd_messages[0]
                msgl = self.event.object.fwd_messages
                astrlist = []
                for a in msgl:
                    astrlist.append(a['text'])
                astr = "\n".join(astrlist)
            url = self.vk.users.get(user_ids=msg['from_id'], fields='photo_max')[0]['photo_max']
            firstname = self.vk.users.get(user_ids=msg['from_id'])[0]['first_name']
            lastname =  self.vk.users.get(user_ids=msg['from_id'])[0]['last_name']
        except:
            self.sendmsg("!error")
            return
        today = datetime.datetime.today().strftime("Дата: %Y-%m-%d, время: %H.%M.%S")
        para = textwrap.wrap(astr, width=30)
        MAX_W, MAX_H = 700, 400
        im = Image.new('RGB', (MAX_W, MAX_H), (0, 0, 0, 0))
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype(fontc,16)
        fontu = ImageFont.truetype(fontc,14)
        current_h, pad = 130, 10
        for line in para:
            w, h = draw.textsize(line, font=font)
            draw.text((250, current_h), line, font=font)
            current_h += h + pad

        img = requests.get(url).content
        f = io.BytesIO(img)

        watermark = Image.open(f).convert("RGBA")
        im.paste(watermark, (10, 100),  watermark)
        draw.text((30, 310), f'{firstname} {lastname}', font=fontu)
        name = f"name{random.randint(0, 1000)}.jpg"
        im.save(name)
        try:
            attachment  = self.uploadphoto(name)
            self.sendmsg("Дэржите цитатку", attachment)
        finally:
            os.remove(name)
