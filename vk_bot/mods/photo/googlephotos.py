from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.modules.upload import Upload
from google_images_download import google_images_download
import random


class GooglePhotos(BasicPlug, Upload):
    doc = "Найти в гугле пикчу по вашему запросу"
    command = ["/гугл", "/пикчи", "/гуглпикчи"]

    def main(self):
        requests = "".join(self.text[1:])
        response = google_images_download.googleimagesdownload()
        arguments = {"keywords": requests, "limit": 25, "no_download": True,
                     "language": "Russian"}
        try:
            url = random.choice(response.download(arguments)[0][requests])
            photos = self.dowloadupload(url)
        except:
            self.sendmsg("Ошибочка")
            return
        self.sendmsg("Таки вот ваша пикча из гугла", photos)
