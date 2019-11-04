import requests
from vk_bot.core.modules.basicplug import BasicPlug
class Forward(BasicPlug):
    doc = "Пересылает фотографию"
    command = ["/перешли"]
    def main(self):
        try:
            attachments = []
            session = requests.Session()
            image_url = self.event.object['attachments'][0]['photo']['sizes'][-1]['url']
            image = session.get(image_url, stream=True)
            photo = self.upload.photo_messages(photos=image.raw)[0]
            attachments.append('photo{}_{}'.format(photo['owner_id'], photo['id']))
            self.sendmsg("Держи!", ','.join(attachments))
        except IndexError:
            self.sendmsg("Мне нужно фото!")