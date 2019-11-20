from vk_bot.core.modules.basicplug import BasicPlug
import re


class Calculator2(BasicPlug):
    doc = "Калькулятор 2.0. Возможно заменит основной"
    command = ["/калькулятор2"]

    def main(self):
        equation = "".join(self.text[1:])
        equation = equation.replace("**", "")
        try:
            int(re.sub(r"[()+*-/]", "", equation))
            self.sendmsg(f"Результат: {eval(equation)}")
        except ValueError:
            self.sendmsg("Использовать в уравнениях можно только +*-/**")
            return
        except ZeroDivisionError:
            self.sendmsg("Планету взорвать хочешь?")
