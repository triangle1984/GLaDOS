from vk_bot.core.modules.basicplug import BacisPlug
from vk_bot import mods
from boltons import iterutils
class GetHelp(BacisPlug):
    doc = "Найти паблики по названию  и скинуть айди"
    command = ["/help", "/хелп", "/начать", "/помощь", "/команды", "/старт"]
    def main(self):
        lhelp = []
        mhelp = "\n"
        allowedtype = ["command", "specialcommand"]
        for moduli in mods.modules:
            if moduli.types in allowedtype and moduli.available_for != "admins":
                lhelp.append(dict(command=moduli.command, doc=moduli.doc))
        lhelp = list(iterutils.chunked_iter(lhelp, 11))
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
        mhelp += f"Всего страниц: {len(lhelp)-1} \n"
        mhelp += "Пример переключения на другую страницу: /хелп 3"
        self.sendmsg(mhelp)
