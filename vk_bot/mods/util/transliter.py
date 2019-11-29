from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.modules.othermethods import OtherMethod


class Weatherandtranslit(BasicPlug, OtherMethod):
    doc = "переведет на русский ваш текст, с любого языка"
    command = ("переводчик",)

    def main(self):
        text = " ".join(self.text[1:])
        response = self.translit(text, "ru")
        self.sendmsg(f"ваш перевод: \n {response}")
