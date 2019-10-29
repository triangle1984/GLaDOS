from vk_bot.core.utils.modutil import BacisPlug
import random
class Searchdoc(BacisPlug):
    doc = "Поиск документов"
    command = ["/док", "/гиф"]
    def main(self):
        text = " ".join(self.text[1:])
        try:
            docs = self.vk.docs.search(q=text, count=200)
            docs = random.choice(docs["items"])
        except IndexError:
            self.sendmsg("Ничего не найдено!")
        docsid = docs["id"]
        docsow = docs["owner_id"]
        docs = f"doc{docsow}_{docsid}"
        self.sendmsg(f"Гифка/документ по заказу - {text}:", docs)