from vk_bot.core.utils.modutil import BacisPlug
import random
class Postsearch(BacisPlug):
    doc = "Поиск постов"
    command = ["/посты"]
    def main(self):
        try:
            text = " ".join(self.text[1:])
            result = random.choice(self.vk2.newsfeed.search(q=text, count=100)["items"])
            owner_id = result["owner_id"]
            idd = result["id"]
        except:
            self.sendmsg("ничо не нашел")
        self.sendmsg("Найденный пост, по вашему запросу", f"wall{owner_id}_{idd}")