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
    check = checktable('waitmeet', 'id2', event.object.from_id)
    if check == None:
        return {'message': 'У тебя нет предложений встречаться!'}
    else:
        tablerm('waitmeet', "id2", event.object.from_id)  
        return {'message':"Вы отклонили предложение"}

def accept(event):
    check = checktable('waitmeet', 'id2', event.object.from_id)
    if check == None:
        return {'message': 'У тебя нет предложений встречаться!'}
    else:
        relationaccept(event.object.from_id)
        tablerm('waitmeet', "id2", event.object.from_id)
        return {'message':"Вы приняли предложение! Поздравляем!"}
def relation(event, vk):
    check = checkrelation('relation', event.object.from_id)
    if check == None:
        return {'message': 'Ты ни с кем не встречаешься :('}
    else:
        userid = checktable('relation', 'id', event.object.from_id)
        if userid == None:
            userid = checktable('relation', 'id2', event.object.from_id)
        if userid['id2'] == event.object.from_id:
            userid = f"*id{userid['id']}({vk.users.get(user_ids=userid['id'], name_case='ins')[0]['first_name']})"
            return {'message':f"Ты встречаешься с {userid}"}
        elif userid['id'] == event.object.from_id:
            userid = f"*id{userid['id2']}({vk.users.get(user_ids=userid['id2'], name_case='ins')[0]['first_name']})"
            return {'message':f"Ты встречаешься с {userid}"}