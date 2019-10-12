from vksql import *
import vk_api
from vk_api.utils import get_random_id
def sendall(event, text,vk, attachment=None):
    if attachment == None:
        text = " ".join(text[1:])
    conn = auth()
    with conn.cursor() as cursor:
        query = f"SELECT * FROM {tablechat}"
        cursor.execute(query)
        result = cursor.fetchall()
        for a in result:
            try:
                vk.messages.send(chat_id=a["id"], random_id=get_random_id(),
                                message=text, attachment=attachment)
            except vk_api.exceptions.ApiError:
                pass
def ban(uid):
    if checktable("ban", "id", uid) == None:
        tableadd("ban", "id", uid)
    return {"message":"Забанен нахой!", "attachment":"video367919273_456240239"}
def unban(uid):
    tablerm("ban", "id", uid)
def checkban(uid):
    if bool(checktable("ban", "id", uid)):
        return "kill him"
def smehdb(ss,uid, db=False):
    check = checktable("smehgen","id", uid)
    if db:
        value = f"id, count, smeh, smehslova"
        add = f"{uid}, {ss.count}, '{ss.smex}', '{ss.smexslova}'"
        if check:
            tablerm("smehgen", "id", uid)
        tableadd("smehgen", value, add)
    else:
        if check:
            ss.count = check["count"]
            ss.smex = check["smeh"]
            ss.smexslova = check["smehslova"]
            return ss
def checkchat(event):
    check = checktable(tablechat, 'id', event.chat_id)
    if check == None:
        tableadd(tablechat, 'id', event.chat_id)
def setmessages(uid):
    conn = auth()
    if checktable('messages', 'id', uid) == None:
        tableadd('messages', 'id, msg', f"{uid}, 0")
    with conn.cursor() as cursor:
        query = f"UPDATE messages SET msg = (msg + 1) WHERE id ='{uid}' "
        cursor.execute(query)
        conn.commit()
def hellosql(chathello, uid, text):
    conn = auth()
    if checktable(chathello, 'id', uid) == None:
        tableadd(chathello, 'id', f"{uid}")
    tableupdate(chathello, "hello", text, f"id = {uid}")
def relationaccept(uid):
    conn = auth()
    with conn.cursor() as cursor:
        query = f"INSERT INTO relation (id,id2) SELECT id,id2 FROM waitmeet where id2 = '{uid}' "
        cursor.execute(query)
        conn.commit()
def checkrelation(table, uid):
    conn = auth()
    with conn.cursor() as cursor:
        query = f"SELECT * FROM {table} WHERE id = '{uid}' or id2 = '{uid}'"
        cursor.execute(query)
    return cursor.fetchone()
def saveload(uid):
    if checktable("prefix", "id", uid) == None:
        tableadd("prefix", "id, name",f"{uid}, 'Дарагуша'")
    if checktable("economy","id", uid) == None:
        tableadd("economy", "id, money", f"{uid}, 0")
    return checktable("prefix", "id", uid)
def update(uid, text, mc):
    conn = auth()
    newname = " ".join(text[1:])
    if len(newname) > 29:
        return {"message":"максимальная длинна префикса: 30 символов"}
    if  "*" in list(newname) or "@" in list(newname) or "[" in list(newname):
        return {"message":"упоминать низя"}
    tableupdate("prefix", "name", newname, f"id = {uid}")
    return {"message":"се ваш префикс сменен"}
