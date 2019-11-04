import pyPrivnote, subprocess
from vk_bot.core.modules.basicplug import BasicPlug
class Genpass(BasicPlug):
    doc = "Сгенерирует пароль"
    command = ["/пароль"]
    def main(self):
        try:
            length = int(self.text[1])
        except:
            length = 64
        if length > 999999:
            length = 99999
        text = f"openssl rand -base64 {length}"
        result = subprocess.check_output(text, shell=True, encoding="utf-8")
        url = pyPrivnote.create_note(result)
        self.sendmsg(f"Пароль тута: {url} . Ссылка на сгорающую записку, которая удалится после просмотра кем либо")