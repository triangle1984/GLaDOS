from vk_bot.core.modules.basicplug import BasicPlug
class Textfrombits(BasicPlug):
    doc = "Расшифровать бинарный код"
    command = ("бинарный1",)
    def main(self):
        text = " ".join(self.text[1:])
        try:
            n = int(text, 2)
        except ValueError:
            self.sendmsg("Введи двоичный код!")
        decode = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode('utf-8', 'surrogatepass') or '\0'
        self.sendmsg(decode)