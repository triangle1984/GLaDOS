from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.modules.upload import Upload
import random
import os


class CamShot(BasicPlug, Upload):
    doc = "Сделать из фотки 'спасибо я кончил'"
    command = ("спасибо",)

    def main(self):
        try:
            link = self.event.object['attachments'][0]['photo']['sizes'][-1]['url']
        except:
            self.sendmsg("пикчонку забыли")
            return
        url = f"http://lunach.ru/?cum=&url={link}&tpl=vk"
        self.sendmsg(f"🌚🌚🌚", self.dowloadupload(url))
