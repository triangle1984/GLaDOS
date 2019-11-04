from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.modules.othermethods import OtherMethod
from vk_bot.core.sql.vksql import *
class Getcommand(BasicPlug, OtherMethod):
    doc = "вытащить команду"
    types = 'commandb'
    @staticmethod
    def getcommand(uid, command):
        if bool(command) == False:
            return
        check = checktable("yourphoto", "id", uid, andd=f"command = '{command}'")
        if check:
            return check["command"]
        else:
            return 666
    def main(self):
        check = checktable("yourphoto", "id", self.uid, andd=f"command = '{self.text[0]}'")
        if check:
            public = check["public"]
            public = public.split(",")
            photos = self.phootowallrandom(public)
            self.sendmsg("Пикча из личного альбома~", photos)
