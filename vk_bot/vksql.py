import pymysql
from token2 import ip, tablechat
from vk_api.utils import get_random_id
from pymysql.cursors import DictCursor
from contextlib import closing
def auth():
    conn = pymysql.connect(host=ip,
                             user="root",
                             password="123",
                             db="mydb",
                             cursorclass=DictCursor)
    return conn
def sendall(event, text, vk):
    text = " ".join(text[1:])
    conn = auth()
    with conn.cursor() as cursor:
        query = f"SELECT * FROM {tablechat}"
        cursor.execute(query)
        result = cursor.fetchall()
        for a in result:
            vk.messages.send(chat_id=a["id"], random_id=get_random_id(),
                             message=text)
def checktable(table, value, should):
    conn = auth()
    with conn.cursor() as cursor:
        query = f"SELECT * FROM {table} WHERE {value} = '{should}'"
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
def tablerm(table, value, rm):
    conn = auth()
    with conn.cursor() as cursor:
        query = f"DELETE FROM {table} WHERE {value} = '{rm}'"
        cursor.execute(query)
        conn.commit()
def saveload(uid, uname):
    conn = auth()
    with conn.cursor() as cursor:
        query = f"SELECT * FROM prefix WHERE id = '{uid}'"
        cursor.execute(query)
        # если нет, записать
        if cursor.fetchone() == None:
            with conn.cursor() as cursor:
                query = f"INSERT INTO prefix (id, name) VALUES ({uid}, '{uname}')"
                cursor.execute(query)
                conn.commit()
        # в любом случае получить запись из бд, даже ежели ее не было и мы
        # только записали
        with conn.cursor() as cursor:
            query = f"SELECT * FROM prefix WHERE id = '{uid}'"
            cursor.execute(query)
            return cursor.fetchone()
def update(uid, name, text):
    saveload(uid, name)
    conn = auth()
    newname = " ".join(text[1:])
    if len(newname) > 29:
        return {"message":"максимальная длинна префикса: 30 символов"}
    with conn.cursor() as cursor:
        query = f"UPDATE prefix SET name = '{newname}' WHERE id = '{uid}'"
        cursor.execute(query)
        conn.commit()
    return {"message":"се ваш префикс сменен"}
def ban(uid):
    conn = auth()
    if checktable("ban", "id", uid) == None:
        with conn.cursor() as cursor:
            query = f"INSERT INTO ban (id) VALUES ({uid})"
            cursor.execute(query)
            conn.commit()
def unban(uid):
    conn = auth()
    with conn.cursor() as cursor:
        query = f"DELETE FROM ban WHERE id = {uid}"
        cursor.execute(query)
        conn.commit()
def checkban(uid):
    conn = auth()
    with conn.cursor() as cursor:
        query = f"SELECT * FROM ban WHERE id = '{uid}'"
        cursor.execute(query)
        if cursor.fetchone():
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
def photoadd(uid, text):
    text = " ".join(text[2])
    if checktable("yourphoto","id", uid):
        tablerm("yourphoto", "id", uid)
    tableadd("yourphoto", "id, idpublic",f"{uid}, {text}")
