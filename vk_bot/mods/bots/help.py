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
            if moduli.types == "command":
                lhelp.append(dict(command=moduli.command, doc=moduli.doc))
        lhelp = list(iterutils.chunked_iter(lhelp, 9))
        lhelp = [dict(command="уходи от", doc="сюда мужик")] + lhelp
        try:
            number = int(self.text[1])
            lhelp2 = lhelp[number]
        except:
            number = 1
            lhelp2 = lhelp[1]
        for moduli in lhelp2:
            mhelp += f"• {', '.join(moduli['command'])} - {moduli['doc']} \n"
        mhelp += f"Страница: {number} \n"
        mhelp += f"Всего страниц: {len(lhelp)-1}"
        self.sendmsg(mhelp)
