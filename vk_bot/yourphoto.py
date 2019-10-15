from vksql import *
from photo import Photo
def nametoid2(vk, names):
    uid = []
    for convert in names:
        r = vk.utils.resolveScreenName(screen_name=convert)
        if r:
            if r["type"] == "group":
                uid.append(f"-{r['object_id']}")
            else:
                uid.append(str(r["object_id"]))
        else:
            uid.append(convert)
    return uid

def photoadd(vk, uid, text, mc, number=1):
    try:
        if text[1] == "список":
            return {"message": getyourphoto(uid)}
        elif text[1] == "удалить":
            return {"message":rmyourphoto(uid, text)}
        else:
            command = text[1]
            public = "".join(text[2:]);public = public.split(",")
            public = ",".join(nametoid2(vk, public))
            number = "".join(text[0])[8:]
            number = int(number)
            if mc["vips"] == False and mc["count"] >=3:
                return {"message":"А больше трех альбомов юзерам низя"}
    except IndexError:
        return {"message":"Гайд по альбомам: https://vk.com/@mtt_resort-gaid-po-lichnym-albomam"}
    except ValueError:
        number = 1
    if checktable("yourphoto","id", uid, andd=f"number = {number}"):
        tablerm("yourphoto", "id", uid, andd=f"number = {number}")
    tableadd("yourphoto", "id,command,public,number",f"{uid}, '{command}','{public}', '{number}'")
    return {"message":f"Ваш личный альбом №{number} настроен, паблики: {public}, команда: {command}"}
def getcommand(uid, command):
    if bool(command) == False:
        return
    check = checktable("yourphoto", "id", uid, andd=f"command = '{command}'")
    if check:
        return check["command"]
    else:
        return 666
def sendyourphoto(vk, text, uid, command):
    check = checktable("yourphoto", "id", uid, andd=f"command = '{command}'")
    if check:
        photos = Photo(vk, text)
        public = check["public"]
        public = public.split(",")
        return photos.yourpic(public)
def getyourphoto(uid):
    conn = auth()
    total = "\n"
    with conn.cursor() as cursor:
        query = f"SELECT * FROM yourphoto WHERE id = '{uid}'"
        cursor.execute(query)
        for row in cursor:
            total += f"Команда: {row['command']}, паблики: {row['public']}, айди: {row['number']}\n"
        return total
def rmyourphoto(uid, text):
    number = text[2]
    if number != "все":
        tablerm("yourphoto", "id", uid, andd=f"number = '{number}'")
    else:
        tablerm("yourphoto", "id", uid)
    return "Се, удалил"
