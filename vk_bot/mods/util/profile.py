from vk_bot.core.modules.basicplug import BacisPlug
from vk_bot.core.sql.vksql import *
class Profile(BacisPlug):
    doc = "Профиль юзера"
    command = ["/профиль"]
    def main(self):
        msg = checktable('messages', 'id', self.uid)["msg"]
        xp = checktable('level', 'id', self.uid)["xp"]
        levelxp = 500
        level = 0
        while xp > levelxp:
            levelxp = levelxp * 2.5
            level += 1
        if self.mc2["admins"]:
            user = "Админ😎"
        elif self.mc2["vips"]:
            user = "Вип🤵"
        else:
            user = "Юзер"
        G = checktable("economy","id", self.uid)["money"]
        self.sendmsg( f"""Твой профиль:
    👦| Роль: {user}
    🔑| Префикс: {self.mc2['prefix']}
    📃| Айди: id{self.uid}
    ✉ | Сообщения: {msg}
    💰| G: {G}$
    🎮| XP: {xp}
    ⭐| Уровень: {level}""")