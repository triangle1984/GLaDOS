from vk_bot.core.sql.vksql import *
from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.modules.othermethods import OtherMethod
import random


class Yourphoto(BasicPlug, OtherMethod):
    command = ("альбомы",)
    doc = "Личные альбомы, вызов без всего покажет справку"
    types = 'specialcommand'

    def main(self):
        while 1:
            rand = random.randint(0, 999999999)
            if checktable("yourphoto", "id", self.uid, andd=f"number = {rand}"):
                continue
            break
        try:
            if self.text[1] == "список":
                self.sendmsg(self.getyourphoto())
                return
            elif self.text[1] == "удалить":
                self.sendmsg(self.rmyourphoto())
                return
            else:
                text = " ".join(self.text[1:])
                stext = text.split("::поиск")
                if len(stext) > 1:
                    public = ",".join(self.groupsearch(7, stext[1]))
                else:
                    public = "".join(self.text[2:])
                    public = public.split(",")
                    public = ",".join(self.nametoid(public))
                command = self.text[1].lower()
                number = "".join(self.text[0])[8:]
                number = int(number)
                if self.mc2["vips"] == False and mc["count"] >= 3:
                    self.sendmsg("А больше трех альбомов юзерам низя")
                    return
        except IndexError:
            self.sendmsg(
                "Гайд по альбомам: https://vk.com/@mtt_resort-gaid-po-lichnym-albomam")
            return
        except ValueError:
            number = rand
        if checktable("yourphoto", "id", self.uid, andd=f"number = {number}"):
            tablerm("yourphoto", "id", self.uid, andd=f"number = {number}")
        tableadd("yourphoto", "id,command,public,number",
                 f"{self.uid}, '{command}','{public}', '{number}'")
        self.sendmsg(
            f"Ваш личный альбом №{number} настроен, паблики: {public}, команда: {command}")
        return

    def getyourphoto(self):
        conn = auth()
        total = "\n"
        with conn.cursor() as cursor:
            query = f"SELECT * FROM yourphoto WHERE id = '{self.uid}'"
            cursor.execute(query)
            for row in cursor:
                total += f"Команда: {row['command']}, паблики: {row['public']}, айди: {row['number']}\n"
            return total

    def rmyourphoto(self):
        number = self.text[2]
        if number != "все":
            tablerm("yourphoto", "id", self.uid, andd=f"number = '{number}'")
        else:
            tablerm("yourphoto", "id", self.uid)
        return "Се, удалил"
