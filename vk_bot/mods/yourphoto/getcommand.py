from vk_bot.core.modules.basicplug import BacisPlug
from vk_bot.photo import Photo
from vk_bot.core.sql.vksql import *
class Getcommand(BacisPlug):
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
            photos = Photo(self.vk2, self.text)
            public = check["public"]
            public = public.split(",")
            photos = photos.yourpic(public)
            self.sendmsg("Пикча из личного альбома~", photos)
