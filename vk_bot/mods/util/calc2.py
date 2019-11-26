from vk_bot.core.modules.basicplug import BasicPlug
import re


class Calculator2(BasicPlug):
    doc = "Полноценный калькулятор"
    command = ("калькулятор", "посчитай", "calc", "скока",)

    def main(self):
        equation = "".join(self.text[1:])
        try:
            int(re.sub(r"[()+*-/e]", "", equation))
            self.sendmsg(f"Результат: {eval(equation)}")
        except ValueError:
            self.sendmsg("Использовать в уравнениях можно только +*-/()e")
            return
        except ZeroDivisionError:
            self.sendmsg("Планету взорвать хочешь?")
