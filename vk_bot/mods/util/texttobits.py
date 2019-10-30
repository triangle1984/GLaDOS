from vk_bot.core.utils.modutil import BacisPlug
class Texttobits(BacisPlug):
    doc = "Зашифровать сообщение в бинарный код"
    command = ["/бинарный0"]
    def main(self):
        text = ' '.join(self.text[1:])
        bits = bin(int.from_bytes(text.encode('utf-8', 'surrogatepass'), 'big'))[2:]
        encode = bits.zfill(8 * ((len(bits) + 7) // 8))
        self.sendmsg(str(encode))