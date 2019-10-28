from PIL import Image, ImageDraw, ImageFont
from loadevn import *
import textwrap, io, requests, random, os, datetime
from vk_bot.modutil import BacisPlug
from vk_bot.core.utils.pillowhelper import Pillowhelper
class Quote(BacisPlug):
    doc = "Сделать цитату по пересланному сообщению"
    command = ["/цитата", "/цитаты"]
    def __checkbackground(self):
        MAX_W, MAX_H = 700, 400
        check = os.path.exists(f"photos/{self.uid}")
        if check:
           self.im = Pillowhelper.resize_image(f'photos/{self.uid}', (MAX_W, MAX_H))
        else:
            self.im = Image.new('RGB', (MAX_W, MAX_H), (0, 0, 0, 0))
    def __setbackground(self):
        try:
            url = self.msg['attachments'][0]['photo']['sizes'][-1]['url']
        except:
            self.sendmsg(f"а пикчу вы видимо забыли")
        os.system(f'wget {url} -O photos/{self.uid}')
    def main(self):
        try:
            if not self.event.object.fwd_messages:
                self.msg = self.event.object.reply_message
                astr = self.msg['text']
            else:
                self.msg = self.event.object.fwd_messages[0]
                self.msgl = self.event.object.fwd_messages
                astrlist = []
                uid = self.msg["from_id"]
                for a in self.msgl:
                    if a["from_id"] == uid:
                        astrlist.append(a['text'])
                astr = "\n".join(astrlist)
            self.uid = self.msg['from_id']
            url = self.vk.users.get(user_ids=self.msg['from_id'], fields='photo_max')[0]['photo_max']
            firstname = self.vk.users.get(user_ids=self.msg['from_id'])[0]['first_name']
            lastname =  self.vk.users.get(user_ids=self.msg['from_id'])[0]['last_name']
        except KeyboardInterrupt:
            self.sendmsg("!error")
            return
        if len(self.text) > 1:
            if self.text[1] == "фон":
                self.__setbackground()
                return
        self.__checkbackground()
        today = datetime.datetime.today().strftime("время: %H:%M:%S, дата: %Y-%m-%d")
        para = textwrap.wrap(astr, width=30)
        draw = ImageDraw.Draw(self.im)
        font = ImageFont.truetype(fontc,16)
        fontu = ImageFont.truetype(fontc,14)
        draw.text((10, 310), f'{firstname} {lastname}', font=fontu)
        draw.text((10, 325), today, font=fontu)
        current_h, pad = 130, 10
        for line in para:
            w, h = draw.textsize(line, font=font)
            draw.text((250, current_h), line, font=font)
            current_h += h + pad

        self.img = requests.get(url).content
        f = io.BytesIO(self.img)

        watermark = Image.open(f).convert("RGBA")
        bigsize = watermark.size[0] * 3, watermark.size[1] * 3
        mask = Image.new('L', bigsize, 0)

        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + bigsize, fill=255)

        mask = mask.resize(watermark.size, Image.ANTIALIAS)
        watermark.putalpha(mask)
        self.im.paste(watermark, (10, 100),  watermark)
        name = f"name{random.randint(0, 1000)}.jpg"
        self.im.save(name)
        try:
            attachment  = self.uploadphoto(name)
            self.sendmsg("Дэржите цитатку", attachment)
        finally:
            os.remove(name)
