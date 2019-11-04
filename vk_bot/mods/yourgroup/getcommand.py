from vk_bot.core.utils.modutil import BacisPlug
from vk_bot.group import Group
from vk_bot.core.sql.vksql import *
class Getcommand(BacisPlug):
    doc = "вытащить команду"
    types = 'commandb'
    @staticmethod
    def getcommand(uid, command):
        if bool(command) == False:
            return
        check = checktable("yourgroup", "id", uid, andd=f"command = '{command}'")
        if check:
            return check["command"]
        else:
            return 666
    def main(self):
        check = checktable("yourgroup", "id", self.uid, andd=f"command = '{self.text[0]}'")
        if check:
            post = Group(self.vk2, self.text)
            public = check["public"]
            public = public.split(",")
            posts = posts.yourpic(public)
            self.sendmsg("Рандомный пост", posts)
