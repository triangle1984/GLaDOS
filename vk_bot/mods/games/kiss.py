#!/usr/bin/env python
from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.modules.upload import Upload
import nekos


class Kiss(BasicPlug, Upload):
    command = ("поцеловать", "цмок", "kiss",)
    doc = "поцеловать юзера"

    def main(self):
        if len(self.text) > 1:
            attachment = self.dowloadupload(nekos.img("kiss"))
            gender = self.vk.users.get(
                user_ids=self.uid, fields="sex")[0]['sex']
            hug = " ".join(self.text[1:])
            if gender == 1:
                act = "поцеловала"
            else:
                act = "поцеловал"
            self.sendmsg(f"{act} {hug}", attachment, split="")
        else:
            self.sendmsg("А кого целовать?")
