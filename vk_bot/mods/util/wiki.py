from vk_bot.core.modules.basicplug import BasicPlug
import wikipedia


class Wiki(BasicPlug):
    doc = "Инфа из вики"
    command = ("вики",)

    def main(self):
        wikipedia.set_lang("ru")
        text = " ".join(self.text[1:])
        try:
            response = wikipedia.summary(text, sentences=3)
            if len(response) < 355:
                response = wikipedia.summary(text, sentences=6)
        except wikipedia.exceptions.DisambiguationError as error:
            response = "Возможно вы имели ввиду: \n"
            response += ", ".join(error.args[1])
        except wikipedia.exceptions.PageError:
            response = "такого нет"
        self.sendmsg(response)
