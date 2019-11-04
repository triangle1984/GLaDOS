from PIL import Image, ImageDraw, ImageFont
from loadevn import *
import textwrap
import io
import requests
import random
import os
import datetime
import argparse
from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.utils.pillowhelper import Pillowhelper
from vk_bot.core.sql.vksql import *


class Quote(BasicPlug):
    doc = "Сделать цитату по пересланному сообщению"
    command = ["/цитата", "/цитаты"]

    def main(self):
        try:
            if self.text[1] == "фон":
                self.setbackground()
            elif self.text[1] == "цвета":
                self.setcolor()
            else:
                self.makequotes()
        except IndexError:
            self.makequotes()

    def checkbackground(self):
        MAX_W, MAX_H = 700, 400
        check = os.path.exists(f"photos/{self.nuid}")
        if check:
            self.im = Image.open(f'photos/{self.nuid}')
        else:
            self.im = Image.new('RGB', (MAX_W, MAX_H), (0, 0, 0, 0))

    def setbackground(self):
        try:
            url = self.event.object['attachments'][0]['photo']['sizes'][-1]['url']
        except:
            self.sendmsg(f"а пикчу вы видимо забыли")
        os.system(f'wget {url} -O photos/{self.uid}.jpg')
        result = Pillowhelper.resize_image(
            f'photos/{self.uid}.jpg', (700, 400))
        result.save(f'photos/{self.uid}.jpg')
        os.system(f'mv photos/{self.uid}.jpg photos/{self.uid}')
        self.sendmsg("установлено")

    def argsforcolor(self):
        args = argparse.ArgumentParser(description="аргументы для цитат")
        args.add_argument("-text", "--text", "-t", default="белый")
        args.add_argument("-data", "--data", "-d", default="белый")
        return args

    def setcolor(self):
        helps = """
        Дроу, это цвета для цитаток
        /цитата цвета -t     - смена цвета для текста в цитате
        /цитата цвета -d     - смена цвета данных в цитатке, т.е дата и имя
        Для юзеров:
            доступно только три цвета - чернй, белый и серый
            собсна, так и можно поменять
            /цитата цвета -t черный -d серый
            сделает вам черный цвет текста и серые данные
        для випов:
            доступны те же цвета шо и у юзеров и такая же их смена
            но!
            для них доступны все цвета этого мира, которые можно получить тут - https://colorscheme.ru/color-converter.html
            мутите себе цвет и копируйте значение на RGBA
            и, пример:
                /цитата цвета -t 255,0,0,1 -d 0,0,0,1 (цифры через запятую и без пробела - обязательно)
                намутит вам белый текст и черные данные
        """
        usercolor = {
            'черный': '0,0,0,1',
            'чёрный': '0,0,0,1',
            'белый': '255,255,255,1',
            'серый': '192,192,192,1'
        }
        try:
            color = self.argsforcolor()
            color = color.parse_args(self.text[2:])
            color.data = color.data.lower()
            color.text = color.text.lower()
        except:
            self.sendmsg(helps)
            return
        if self.mc2['vips'] == False:
            if color.text not in usercolor or color.data not in usercolor:
                self.sendmsg(helps)
                return
        try:
            if len(color.data.split(",")) != 4:
                color.data = usercolor[color.data]
            if len(color.text.split(",")) != 4:
                color.text = usercolor[color.text]
        except:
            self.sendmsg(helps)
            return
        if checktable('quotes', 'uid', self.uid):
            tablerm("quotes", "uid", self.uid)
        tableadd('quotes', 'uid, yourtext, text',
                 f"{self.uid}, '{color.text}', '{color.data}'")
        self.sendmsg(
            f"Вы установили цвета, для даты: {color.data}, для текста: {color.text}")

    def getcolor(self):
        self.text = (255, 255, 255, 1)
        self.data = (255, 255, 255, 1)
        check = checktable("quotes", "uid", self.uid)
        if check:
            text = check["yourtext"].split(",")
            data = check["text"].split(",")
            self.text = tuple(map(int, text))
            self.data = tuple(map(int, data))

    def makequotes(self):
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
            self.nuid = self.msg['from_id']
            url = self.vk.users.get(user_ids=self.msg['from_id'], fields='photo_max')[
                0]['photo_max']
            firstname = self.vk.users.get(user_ids=self.msg['from_id'])[
                0]['first_name']
            lastname = self.vk.users.get(user_ids=self.msg['from_id'])[
                0]['last_name']
        except KeyboardInterrupt:
            self.sendmsg("!error")
            return
        self.checkbackground()
        self.getcolor()
        today = datetime.datetime.today().strftime("время: %H:%M:%S")
        today2 = datetime.datetime.today().strftime("дата: %Y-%m-%d")
        para = textwrap.wrap(astr, width=30)
        draw = ImageDraw.Draw(self.im)
        font = ImageFont.truetype(fontc, 18)
        fontu = ImageFont.truetype(fontc, 16)
        draw.text((10, 310), f'{firstname} {lastname}',
                  font=fontu, fill=self.data)
        draw.text((10, 325), today, font=fontu, fill=self.data)
        draw.text((10, 340), today2, font=fontu, fill=self.data)
        current_h, pad = 170, 10
        for line in para:
            w, h = draw.textsize(line, font=font)
            draw.text(((850 - w) / 2, current_h),
                      line, font=font, fill=self.text)
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
            attachment = self.uploadphoto(name)
            self.sendmsg("Дэржите цитатку", attachment)
        finally:
            os.remove(name)
