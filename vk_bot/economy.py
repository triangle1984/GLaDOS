from vksql import *
def givemoney(uid,mc2):
    if mc2["admins"]:
        money = 200
    elif mc2["vips"]:
        money = 150
    else:
        money = 50
    tableupdate("economy","money", f"money + {money}", uid, add=True)
def economylobby(uid, mc2, text):
    try:
        if text[1] == "магазин":
            return {"message":"а здеся ничаво нет)0"}
    except IndexError:
        return {"message": "Будущая подсказка буит тут"}
