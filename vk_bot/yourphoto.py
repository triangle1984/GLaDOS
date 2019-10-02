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
        else:
            command = text[1]
            public = "".join(text[2:]);public = public.split(",")
            public = ",".join(nametoid2(vk, public))
            if number != 1:
                number = "".join(text[0])[8:]
            number = int(number)
    except IndexError:
        return {"message": """ Это личные альбомы. Их смысл в том, что каждый человек,
                может создать себе личную команду с пикчами из указанных пабликов.
                Эта команда будет работать только у него(хотя другой человек может создать свою, с таким же названием, конфликта не будет)
                /альбомы <команда> <айди пабликов, через запятую>
                например: /альбомы /шедевр mtt_resort,rimworld (паблик можно и один указать)
                и потом можно ее вызывать на /шедевр
                так же можно использовать ключи для количества
                /шедевр -c 10 - скинет 10 пикч с вашей команды
                (10 максимум в вк)
                Так же, /альбомы список - выведет список ваших альбомов
                так же, ежели вы не вип, то создание альбома заменяет старый.
                А теперь о випах:
                випы могут делать бесконечное количество альбомов
                Т.е: вызов /альбомы1 /ри rire_re и /альбомы2 /рим rimworld
                создаст две команды, /рим и /ри которые можно вызывать когда угодно
                и так до бесконечности, лишь указывайте разные числа.
                Ежели указать такое же число, какое и есть у одной из команд - заменится
                """}
    except ValueError:
        return {"message": "номер альбома должон быть цифровым"}
    if checktable("vips", "id", uid) == None:
        tablerm("yourphoto", "id", uid)
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
