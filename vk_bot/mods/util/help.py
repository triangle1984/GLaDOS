from vk_bot.core.utils.modutil import BacisPlug
from vk_bot import mods
from boltons import iterutils
class GetHelp(BacisPlug):
    doc = "Найти паблики по названию  и скинуть айди"
    command = ["/хелп2"]
    def main(self):
        lhelp = []
        mhelp = "\n"
        for moduli in mods.modules:
            lhelp.append(dict(command=moduli.command[0], doc=moduli.doc))
        lhelp = list(iterutils.chunked_iter(lhelp, 5))
        try:
            number = int(self.text[1])
            lhelp2 = lhelp[number]
            nubmer = 0
        except:
            self.sendmsg("такого номера справки нет. Смотрим 0ой")
            lhelp2 = lhelp[0]
        for moduli in lhelp2:
            mhelp += f"Команда: {moduli['command']}, хелп: {moduli['doc']} \n"
        mhelp += f"Номер: {number}"
        self.sendmsg(mhelp)
