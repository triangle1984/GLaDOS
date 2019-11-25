from vk_bot.core.modules.basicplug import BasicPlug
import wikipedia
class Wiki(BasicPlug):
    doc = "Инфа из вики"
    command = ("вики",)
    def main(self):
        wikipedia.set_lang("ru")
        text = " ".join(self.text[1:])
        try:
            wikiotvet = wikipedia.summary(text, sentences=3)
            if len(wikiotvet) < 355:
                wikiotvet = wikipedia.summary(text, sentences=6)
        except wikipedia.exceptions.DisambiguationError:
            wikiotvet = "точнее, пожалуйста"
        except wikipedia.exceptions.PageError:
            wikiotvet = "такого нет"
        self.sendmsg(wikiotvet)
