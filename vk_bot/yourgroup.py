from vksql import checktable, tablerm, tableadd
from yourphoto import nametoid2
import random
def groupadd(vk, uid, text):
    try:
        command = text[1]
        public = "".join(text[2:]);public = public.split(",")
        public = ",".join(nametoid2(vk, public))
    except IndexError:
        return {"message": """Тут вы можете указать группы, из которых хотите брать рандомный пост.
                /группы <команда> <айди пабликов, через запятую>
                например: /альбомы /шедевр mtt_resort,rimworld (паблик можно и один указать)
                и потом можно ее вызывать на /шедевр"""}
    if checktable("yourgroup","id", uid):
        tablerm("yourgroup", "id", uid)
    tableadd("yourgroup", "id,command,public",f"{uid}, '{command}','{public}'")
    return {"message":f"Ваша личная группа настроена, паблики: {public}, команда: {command}"}
def getcommandpost(uid):
    check = checktable("yourgroup", "id", uid)
    if check:
        return check["command"]
    else:
        return 666


def postwallrandom(public, vk):
    post2 = []
    public = str(random.choice(public))
    max_num = vk.wall.get(owner_id=public, count=0)['count']
    num = random.randint(0, max_num)
    post = vk.wall.get(owner_id=public, count=1, offset=num)['items'][0]['id']
    post2.append(f"wall{public}_{post}")
    post2 = ",".join(post2)
    return post2

def yourpost(vk, public):
    post = postwallrandom(public, vk)
    return {"message":"Рандомный пост!", "attachment":post}

def sendyourpost(vk, text, uid):
    check = checktable("yourgroup", "id", uid)
    if check:
        public = check["public"]
        public = public.split(",")
        return yourpost(vk, public)