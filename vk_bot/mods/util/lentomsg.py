from vk_bot.core.utils.modutil import BacisPlug
class Lentomsg(BacisPlug):
    doc = "Длина сообщения"
    command = ["/длина"]
    def main(self):
        text = " ".join(self.text[1:])
        length = len(text)
        self.sendmsg(f"Символов в сообщении: {length}")