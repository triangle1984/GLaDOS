import pymysql
from token2 import ip
from pymysql.cursors import DictCursor
from contextlib import closing
def auth():
    conn = pymysql.connect(host=ip,
                             user="root",
                             password="123",
                             db="mydb",
                             cursorclass=DictCursor)
    return conn
def checktable(table, value, should):
    conn = auth()
    with conn.cursor() as cursor:
        query = f"SELECT * FROM {table} WHERE {value} = '{should}'"
        cursor.execute(query)
    return cursor.fetchone()
def tableadd(table, value, add):
    conn = auth()
    with conn.cursor() as cursor:
        query = f"INSERT INTO {table} ({value}) VALUES ({add})"
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
