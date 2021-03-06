from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.sql.sqlgame import hellosql
from vk_api.utils import get_random_id
from vk_bot.config import *
class Hello(BasicPlug):
    doc = "Установка приветствий для новых участников беседы"
    command = ("приветствие",)
    def main(self):
        text = " ".join(self.text[1:])
        if text == "":
            return
        if self.event.object['attachments']:
            self.vk.messages.send(chat_id=self.event.chat_id, random_id=get_random_id(),  message="Никаких вложений! Только текст")
        elif len(text) > 500:
            self.vk.messages.send(chat_id=self.event.chat_id, random_id=get_random_id(),  message="Не больше 500 знаков!")
        else:
            response = hellosql('chathello', self.event.chat_id, text)
            self.sendmsg(f"Вы установили приветствие: \"{text}\"")