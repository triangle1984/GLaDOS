from vk_bot.core.modules.basicplug import BasicPlug
import math
class Calculator(BasicPlug):
    doc = "Калькулятор"
    command = ["/калькулятор"]
    def main(self):
        try:
            x = self.text[1]; x = int(x)
            encalc = self.text[2]; encalc = encalc.lower()
            y = self.text[3]; y = int(y)
        except:
            self.sendmsg("""Пример команды: /калькулятор 2 + 2
            Использовать можно только 2 числа, и только через пробел""")
            return
        if encalc == "+" or encalc == "сложение":
            result = x + y
        elif encalc == "-" or encalc == "вычитание":
            result = x - y
        elif encalc == "*" or encalc == "умножение":
            result = x * y
        elif encalc == "**" or encalc == "степень" or encalc == "^":
            if x > 999 or y > 999:
                return
            result = x ** y
        elif encalc == "/":
            try:
                x / y
            except ZeroDivisionError:
                result = "взорвать планету хочешь?"
        elif encalc == "корень":
            result = math.sqrt(x), math.sqrt(y)
        elif encalc == "синус":
            result = math.sin(x), math.sin(y)
        elif encalc == "косинус":
            result = math.cos(x), math.cos(y)
        else:
            return
        self.sendmsg(f"Ваш результат: {result}")