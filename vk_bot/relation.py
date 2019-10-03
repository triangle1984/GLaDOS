import vk_api
from vk_api.utils import get_random_id
from vksql import *

def relationmeet(text, vk, event):
    check = checkrelation('waitmeet', event.object.from_id)
    if check == None:
        check = checkrelation('relation', event.object.from_id)
        if check == None:
            userid = "".join(text[2][3:])
            userid = userid.split('|')[0]
            tableadd("waitmeet", "id, id2", (f"{event.object.from_id}, {userid}"))
            vk.messages.send(user_id=int(userid), random_id=get_random_id(),
                                    message=f"*id{event.object.from_id}(Пользователь) предложил тебе встречаться!\nНапиши: '/отношения принять' или '/отношения отклонить'")
        else:
            return {"message": "Ай-яй-яй! Изменять нехорошо"}
    else:
        return {"message": "Ты уже отправил приглашение!"}
def reject(event):
    check = checktable('waitmeet', 'id', event.object.from_id)
    if check == None:
        return {'message': 'У тебя нет предложений встречаться!'}
    else:
        tablerm('waitmeet', "id2", event.object.from_id)  
        return {'message':"Вы отклонили предложение"}

def accept(event):
    check = checktable('waitmeet', 'id', event.object.from_id)
    if check == None:
        return {'message': 'У тебя нет предложений встречаться!'}
    else:
        relationaccept(event.object.from_id)
        tablerm('waitmeet', "id2", event.object.from_id)
        return {'message':"Вы приняли предложение! Поздравляем!"}
def relation(event):
    check = checkrelation('relation', event.object.from_id)
    if check == None:
        return {'message': 'Ты ни с кем не встречаешься :('}
    else:
        userid = checktable('relation', 'id', event.object.from_id)
        return {'message':f"Ты встречаешься с *id{userid}"}