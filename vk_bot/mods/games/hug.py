#!/usr/bin/env python
from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.modules.upload import Upload
import nekos


class Hug(BasicPlug, Upload):
    command = ("обнять", "обнимашки", "hug",)
    doc = "обнять юзера"

    def main(self):
        if len(self.text) > 1:
            attachment = self.dowloadupload(nekos.img("hug"))
            gender = self.vk.users.get(
                user_ids=self.uid, fields="sex")[0]['sex']
            hug = ",".join(self.text[1:])
            if gender == 1:
                act = "обняла"
            else:
                act = "обнял"
            self.sendmsg(f"{act} {hug}", attachment)
        else:
            self.sendmsg("А кого обнимать?")
