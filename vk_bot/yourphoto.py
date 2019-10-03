from vksql import checktable, tablerm, tableadd, tablecount, auth
from photo import yourpic
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

def photoadd(vk, uid, text, number=1):
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
            if checktable("vips","id", uid) == None and tablecount("yourphoto", "id", uid) >=3:
                return {"message":"А больше трех альбомов юзерам низя"}
    except IndexError:
        return {"message": """ Это личные альбомы. Их смысл в том, что каждый человек,
                может создать себе личную команду с пикчами из указанных пабликов.
                Эта команда будет работать только у него(хотя другой человек может создать свою, с таким же названием, конфликта не будет)
                /альбомы <команда> <айди пабликов, через запятую>
                например: /альбомы /шедевр mtt_resort,rimworld (паблик можно и один указать)
                и потом можно ее вызывать на /шедевр
                но ежели вы вызовите эту команду(альбомы), то она перезапишет старый альбом
                поэтому, ежели хотите несколько - используйте на конце своеобразный айди
                т.е: /альбомы2 /рим rimworld
                и /альбомы3 /ри rire_re
                позволят существовать трем разным командам одновременно.
                Айди на конце могут быть любые и любой длины, ежели указать неправильно
                например /альбомыхуй - то поставится дефолтное значение: 1
                И ежели указать тот же айдишник, шо  и есть у какой-то вашей команды - перезапишется
                Ограничение по количеству альбомов не випу - 3
                так же можно использовать ключи для количества
                /шедевр -c 10 - скинет 10 пикч с вашей команды
                (10 максимум в вк)
                Так же, /альбомы список - выведет список ваших альбомов
                Так же, /альбомы удалить *айди из /альбомы список* удалит альбом
                либо, /альбомы удалить все - удалит все ваши альбомы
                """}
    except ValueError:
        number = 1
    if checktable("yourphoto","id", uid, andd=f"number = {number}"):
        tablerm("yourphoto", "id", uid, andd=f"number = {number}")
    tableadd("yourphoto", "id,command,public,number",f"{uid}, '{command}','{public}', '{number}'")
    return {"message":f"Ваш личный альбом №{number} настроен, паблики: {public}, команда: {command}"}
def getcommand(uid, command):
    check = checktable("yourphoto", "id", uid, andd=f"command = '{command}'")
    if check:
        return check["command"]
    else:
        return 666
def sendyourphoto(vk, text, uid, command):
    check = checktable("yourphoto", "id", uid, andd=f"command = '{command}'")
    if check:
        public = check["public"]
        public = public.split(",")
        return yourpic(vk, text, public)
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
