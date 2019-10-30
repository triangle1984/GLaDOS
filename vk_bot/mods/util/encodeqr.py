import requests, vk_api
from vk_bot.core.utils.modutil import BacisPlug
class Encodeqr(BacisPlug):
    doc = "Зашифровать текст в qrcode"
    command = ["/encodeqr"]
    def main(self):
        try:
            attachments = []
            session = requests.Session()
            text = " ".join(self.text[1:])
            image_url = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={text}"
            image = session.get(image_url, stream=True)
            photo = self.upload.photo_messages(photos=image.raw)[0]
            attachments.append('photo{}_{}'.format(photo['owner_id'], photo['id']))
            self.sendmsg("Держи!", ','.join(attachments))
        except vk_api.exceptions.ApiError:
            self.sendmsg("Только текст!")