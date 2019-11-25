from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.modules.upload import Upload
import os
import time


class Hmux(BasicPlug, Upload):
    doc = "Жмыхнуть фотку."
    command = ("жмых",)

    def main(self):
        helps = """
        Жмыхалка фоток, хорошо ломает психику неподготовленным личностям.
        Жмыхает вашу прикрепленную фотку, так же
        можно передавать степень жмыхнутости, пример:
            /жмых 55 55
            /жмых 59 80
            чем ниже значения, тем сильнее жмыханет
            максимум для одного из знчений - 100
            а дефолт - 40 40
        """
        try:
            url = self.event.object['attachments'][0]['photo']['sizes'][-1]['url']
        except IndexError:
            self.sendmsg(helps)
            return
        name = self.dowloadfile(url)['name']
        outname = f"{time.time_ns()}.out.png"
        x = 50
        y = 50
        if len(self.text) > 2:
            try:
                x = int(self.text[1])
                y = int(self.text[2])
            except ValueError:
                self.sendmsg(helps)
        if x > 100 or y > 100:
            self.sendmsg(helps)
        os.system(f"convert {name} -liquid-rescale {y}x{x}%\! {outname}")
        os.remove(name)
        self.sendmsg("Держи", self.uploadphoto(outname))
