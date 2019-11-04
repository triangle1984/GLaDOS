from vk_bot.core.utils.modutil import BacisPlug
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
            posts = posts.yourpost(public)
            self.sendmsg("Рандомный пост", posts)
class Group:
    def __init__(self, vk,text):
        self.vk = vk
        self.text = text
    def groupwallrandom(self, groups, albid="wall"):
        post2 = []
        try:
            group_id = random.choice(groups)
            max_num = self.vk.wall.get(owner_id=group_id, album_id=albid, count=0)['count']
            num = random.randint(0, max_num)
            post = self.vk.wall.get(owner_id=group_id, count=1, offset=num)['items'][0]['id']
            post2.append(f"wall{group_id}_{post}")
        except KeyboardInterrupt:
            self.sendmsg("!error от вк");return
        photo2 = ",".join(post2)
        return photo2
    def yourpost(self, public):
        post = self.groupwallrandom(public)
        return post
