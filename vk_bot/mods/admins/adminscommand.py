from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.sql.vksql import *
from vk_bot.core.sql.sqlgame import *
class Admins(BasicPlug):
    command = ["/бан", "/разбан:", "/вип"]
    doc = "Забанить или разбанить"
    available_for = "admins"
    def main(self):
        requests = self.text[0]
        try:
            uid = event.object.reply_message['from_id']
        except:
            print(".")
            None
        if requests == "/бан":
            tableadd("ban", "id", uid, one=True)
            self.sendmsg("забанен нахой", "video367919273_456240239")
        elif requests == "/разбан":
            tablerm("ban", "id", uid)
        elif requests == "/вип":
            tableadd("vips", "id", event.object.reply_message['from_id'])
        elif requests == "/рассылка":
            sendall(self.event, self.text, self.vk)
