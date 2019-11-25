from vk_bot.core.sql.vksql import *
from vk_bot.core.sql.sqlgame import *


def sqlcache(mc, uid):
    uid = str(uid)
    if uid in mc:
        """
        Вытаскивание из кеша происходит после каждой команды
        поэтому, ежели в кеше уже есть данные на этот айдишник
        ничего не обновлять, а просто вернуть эти данные
        поэтому, щобы заставить обновить данные в кеше - удалите его айдишник оттуда
        """
        None
    else:
        # вызывается, ежели в кеше на данного юзера ничо нет
        saveload(uid)
        prefix = checktable("prefix", "id", uid)["name"]
        vips = bool(checktable("vips", "id", uid))
        admins = bool(checktable("admins", "id", uid))
        count = tablecount("yourphoto", "id", uid)
        ban = bool(checktable("ban", "id", uid))
        mc.set(uid, {"vips": vips,
                     "prefix": prefix,
                     "admins": admins,
                     "count": count,
                     "user": True,
                     "ban": ban})
    # вернуть данные из кеша
    return mc.get(uid)
