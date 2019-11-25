import requests
from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.modules.upload import Upload


class Forward(BasicPlug, Upload):
    doc = "Пересылает фотографию"
    command = ("перешли",)

    def main(self):
        try:
            image_url = self.event.object['attachments'][0]['photo']['sizes'][-1]['url']
            self.sendmsg("Держи!", self.dowloadupload(image_url))
        except IndexError:
            self.sendmsg("Мне нужно фото!")
