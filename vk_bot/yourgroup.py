from vksql import checktable, tablerm, tableadd, tablecount, auth
from yourphoto import nametoid2
import random
def groupadd(vk, uid, text, mc, number=1):
    try:
        if text[1] == "список":
            return {"message": getyourpost(uid)}
        elif text[1] == "удалить":
            return {"message":rmyourpost(uid, text)}
        else:
            command = text[1]
            public = "".join(text[2:]);public = public.split(",")
            public = ",".join(nametoid2(vk, public))
            number = "".join(text[0])[7:]
            number = int(number)
            if mc["vips"] == False and mc["count"] >=3:
                return {"message":"А больше трех групп юзерам низя"}
    except IndexError:
        return {"message": """Это личные группы. Работают точно так же, как и альбомы, но вместо картинок - отправляет рандомные посты"""}
    except ValueError:
        number = 1
    if checktable("yourgroup","id", uid, andd=f"number = {number}"):
        tablerm("yourgroup", "id", uid, andd=f"number = {number}")
    tableadd("yourgroup", "id,command,public,number",f"{uid}, '{command}','{public}', '{number}'")
    return {"message":f"Ваш личная группа №{number} настроена, паблики: {public}, команда: {command}"}
def getcommandpost(uid, command):
    check = checktable("yourgroup", "id", uid, andd=f"command = '{command}'")
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

def sendyourpost(vk, text, uid, command):
    check = checktable("yourgroup", "id", uid, andd=f"command = '{command}'")
    if check:
        public = check["public"]
        public = public.split(",")
        return yourpost(vk, public)

def getyourpost(uid):
    conn = auth()
    total = "\n"
    with conn.cursor() as cursor:
        query = f"SELECT * FROM yourgroup WHERE id = '{uid}'"
        cursor.execute(query)
        for row in cursor:
            total += f"Команда: {row['command']}, паблики: {row['public']}, айди: {row['number']}\n"
        return total

def rmyourpost(uid, text):
    number = text[2]
    if number != "все":
        tablerm("yourgroup", "id", uid, andd=f"number = '{number}'")
    else:
        tablerm("yourgroup", "id", uid)
    return "Се, удалил"
