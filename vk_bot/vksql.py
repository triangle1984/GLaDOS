import pymysql, vk_api
from token2 import ip, tablechat
from vk_api.utils import get_random_id
from pymysql.cursors import DictCursor
from contextlib import closing
from photo import yourpic
from token2 import *
def auth():
    conn = pymysql.connect(host=ip,
                             user="bot",
                             password="123",
                             db="mydb",
                             cursorclass=DictCursor)
    return conn
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
                break
def tablecount(table, value, count):
    conn = auth()
    with conn.cursor() as cursor:
        query = f"SELECT COUNT(*) FROM {table} WHERE {value} = '{count}'"
        cursor.execute(query)
        return cursor.fetchone()["COUNT(*)"]
def checktable(table, value, should, andd=False):
    conn = auth()
    with conn.cursor() as cursor:
        query = f"SELECT * FROM {table} WHERE {value} = '{should}'"
        if andd:
            query = f"SELECT * FROM {table} WHERE {value} = '{should}' and {andd}"
        cursor.execute(query)
    return cursor.fetchone()
def tableadd(table, value, add, one=False):
    conn = auth()
    try:
        with conn.cursor() as cursor:
            query = f"INSERT INTO {table} ({value}) VALUES ({add})"
            cursor.execute(query)
            conn.commit()
    except pymysql.err.InternalError:
        return
def tablerm(table, value, rm, andd=False):
    conn = auth()
    with conn.cursor() as cursor:
        query = f"DELETE FROM {table} WHERE {value} = '{rm}'"
        if andd:
            query = f"DELETE FROM {table} WHERE {value} = '{rm}' and {andd}"
        cursor.execute(query)
        conn.commit()
def tableupdate(table, value, should, where):
    conn = auth()
    with conn.cursor() as cursor:
        query = f"UPDATE {table} SET {value} = '{should}' WHERE {where}"
        cursor.execute(query)
        conn.commit()
def saveload(uid):
    if checktable("prefix", "id", uid) == None:
        tableadd("prefix", "id, name",f"{uid}, 'Дарагуша'")
    return checktable("prefix", "id", uid)
def update(uid, text):
    conn = auth()
    newname = " ".join(text[1:])
    if len(newname) > 29:
        return {"message":"максимальная длинна префикса: 30 символов"}
    if  "*" in list(newname) or "@" in list(newname) or "[" in list(newname):
        return {"message":"упоминать низя"}
    tableupdate("prefix", "name", newname, f"id = {uid}")
    return {"message":"се ваш префикс сменен"}
def ban(uid):
    if checktable("ban", "id", uid) == None:
        tableadd("ban", "id", uid)
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
    if checktable('messages', 'id', uid) == None:
        tableadd('messages', 'id, msg', f"{uid}, 0")
    tableupdate("messages","msg", "(msg + 1)", f"id = {uid}")
def hellosql(chathello, uid, text):
    conn = auth()
    if checktable(chathello, 'id', uid) == None:
        tableadd(chathello, 'id', f"{uid}")
    with conn.cursor() as cursor:
        query = f"UPDATE {chathello} SET hello = '{text}' WHERE id ='{uid}' "
        cursor.execute(query)
        conn.commit()
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
