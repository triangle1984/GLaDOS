from vk_bot.core.modules.basicplug import BacisPlug
import random
class Video(BacisPlug):
    doc = "Поиск видео"
    command = ["/видео"]
    def main(self):
        text = " ".join(self.text[1:])
        try:
            video = self.vk2.video.search(q=text, count=50)
            video = random.choice(video["items"])
            videoid = video["id"]
            videoow = video["owner_id"]
        except IndexError:
            self.sendmsg("ничо не найдено")
        video = f"video{videoow}_{videoid}"
        self.sendmsg(f"Ведосик по заказу - {text}:", video)