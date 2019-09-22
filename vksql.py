import pymysql
from pymysql.cursors import DictCursor
from contextlib import closing
def auth():
    # не пытайтесь подключиться, айпишники локальные
    conn = pymysql.connect(host="10.59.111.63",
                             user="root",
                             password="123",
                             db="mydb",
                             cursorclass=DictCursor)
    return conn
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
