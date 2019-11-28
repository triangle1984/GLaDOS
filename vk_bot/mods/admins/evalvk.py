from vk_bot.core.modules.basicplug import BasicPlug


class Eval(BasicPlug):
    command = ("eval", "евал",)
    available_for = "admins"

    def main(self):
        text = " ".join(self.text[1:])
        self.sendmsg(f"Результат: {eval(text)}")
