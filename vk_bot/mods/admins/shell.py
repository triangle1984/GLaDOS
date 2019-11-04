from vk_bot.core.modules.basicplug import BasicPlug
import subprocess
class Shell(BasicPlug):
    command = ["/шелл"]
    doc = "Выполнить команду в шелле"
    available_for = "admins"
    def main(self):
        text = " ".join(self.text[1:])
        try:
            result = subprocess.check_output(text, shell=True, encoding="utf-8")
        except:
            self.sendmsg("!error")
            return
        self.sendmsg(result)
