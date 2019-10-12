from vksql import *
import random
def givemoney(uid,mc2):
    if mc2["admins"]:
        money = 200
    elif mc2["vips"]:
        money = 150
    else:
        money = 50
    tableupdate("economy","money", f"money + {money}", f"id = {uid}", add=True)
def economylobby(uid, mc2, text):
    try:
        if text[1] == "магазин":
            return {"message":"а здеся ничаво нет)0"}
    except IndexError:
        return {"message": "Будущая подсказка буит тут"}
def economygame1(uid, text):
    try:
        listcolor = ['зеленый','красный', 'белый']
        ucolor = text[1]
        money = int(text[2])
        b = random.randrange(1, 100)
        if checktable('economy', 'id', uid)['money'] < money:
            return {"message": "Не хватает денег!"}
        if money <= 0:
            return {"message": "Введи число больше 0!"}
        if ucolor not in listcolor:
            return {"message": "Введи цвет: зеленый, белый или красный"}
        if b <= 15:
            color, multiply = "зеленый", 8
        elif b <= 40:
            color, multiply = "белый", 2
        else:
            color, multiply = "красный", 2
        if ucolor == color:
            tableupdate("economy", "money", f"money + {money * multiply}", f"id = '{uid}'", add=True)
            return {"message": f"Выпал {color}, ваше бабло: {money * multiply}"}
        else:
            tableupdate("economy", "money", f"money - {money}", f"id = '{uid}'", add=True)
            return {"message": "Вы проиграли"}
    except ValueError:
        return {"message": "Введи число!"}
