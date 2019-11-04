from vk_bot.core.sql.vksql import *
from vk_bot.photo import Photo
from vk_bot.core.utils.modutil import BacisPlug
import random
class Yourgroup(BacisPlug):
    command = ["/группы"]
    doc = "Личные группы, вызов без всего покажет справку"
    types = 'specialcommand'
    def nametoid2(self, names):
        uid = []
        for convert in names:
            r = self.vk.utils.resolveScreenName(screen_name=convert)
            if r:
                if r["type"] == "group":
                    uid.append(f"-{r['object_id']}")
                else:
                    uid.append(str(r["object_id"]))
            else:
                uid.append(convert)
        return uid

    def main(self):
        number = 1
        try:
            if self.text[1] == "список":
                self.sendmsg(self.getyourgroup());return
            elif self.text[1] == "удалить":
                self.sendmsg(self.rmyourgroup());return
            else:
                command = self.text[1].lower()
                public = "".join(self.text[2:]);public = public.split(",")
                public = ",".join(self.nametoid2(public))
                number = "".join(self.text[0])[8:]
                number = int(number)
                if self.mc2["vips"] == False and mc["count"] >=3:
                    self.sendmsg("А больше трех групп юзерам низя");return
        except IndexError:
            self.sendmsg("Работают точно так-же, как и альбомы: https://self.vk.com/@mtt_resort-gaid-po-lichnym-albomam");return
        except ValueError:
            number = 1
        if checktable("yourgroup","id", self.uid, andd=f"number = {number}"):
            tablerm("yourgroup", "id", self.uid, andd=f"number = {number}")
        tableadd("yourgroup", "id,command,public,number",f"{self.uid}, '{command}','{public}', '{number}'")
        self.sendmsg(f"Ваша личная группа №{number} настроена, паблики: {public}, команда: {command}");return
    def getyourgroup(self):
        conn = auth()
        total = "\n"
        with conn.cursor() as cursor:
            query = f"SELECT * FROM yourgroup WHERE id = '{self.uid}'"
            cursor.execute(query)
            for row in cursor:
                total += f"Команда: {row['command']}, паблики: {row['public']}, айди: {row['number']}\n"
            return total
    def rmyourgroup(self):
        number = self.text[2]
        if number != "все":
            tablerm("yourgroup", "id", self.uid, andd=f"number = '{number}'")
        else:
            tablerm("yourgroup", "id", self.uid)
        return "Се, удалил"
