from loadevn import recipient
from vk_api.utils import get_random_id
from vk_bot.core.modules.basicplug import BasicPlug
class Lentomsg(BasicPlug):
    doc = "Отправить сообщение админу"
    command = ("репорт",)
    def main(self):
        text = " ".join(self.text[1:])
        if text == "":
            self.sendmsg("Введите текст!")
        else:
            idjoin = f"*id{self.event.object.from_id} (Пользователь)"
            self.vk.messages.send(user_id=recipient, random_id=get_random_id(), attachment="photo271595905_457261640",
                            message=f'{idjoin} отправил сообщение: {text}')