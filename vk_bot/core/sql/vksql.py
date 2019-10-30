import pymysql
from pymysql.cursors import DictCursor
from contextlib import closing
from vk_bot.loadevn import *
def auth():
    conn = pymysql.connect(host=ip,
                             user=user,
                             password=password,
                             db=db,
                             cursorclass=DictCursor)
    return conn
def tablecount(table, value, count):
    try:
        conn = auth()
        with conn.cursor() as cursor:
            query = f"SELECT COUNT(*) FROM {table} WHERE {value} = '{count}'"
            cursor.execute(query)
            return cursor.fetchone()["COUNT(*)"]
    except:
        return
def checktable(table, value, should, andd=False):
    try:
        conn = auth()
        with conn.cursor() as cursor:
            query = f"SELECT * FROM {table} WHERE {value} = '{should}'"
            if andd:
                query = f"SELECT * FROM {table} WHERE {value} = '{should}' and {andd}"
            cursor.execute(query)
        return cursor.fetchone()
    except:
        return
def tableadd(table, value, add, one=False, onerm=False):
    try:
        conn = auth()
        try:
            with conn.cursor() as cursor:
                query = f"INSERT INTO {table} ({value}) VALUES ({add})"
                if one or onerm:
                    if bool(checktable(table, value, add)):
                        if one:
                            return
                        elif onerm:
                            tablerm(table, value, add)
                cursor.execute(query)
                conn.commit()
        except pymysql.err.InternalError:
            return
    except:
        return
def tablerm(table, value, rm, andd=False):
    try:
        conn = auth()
        with conn.cursor() as cursor:
            query = f"DELETE FROM {table} WHERE {value} = '{rm}'"
            if andd:
                query = f"DELETE FROM {table} WHERE {value} = '{rm}' and {andd}"
            cursor.execute(query)
            conn.commit()
    except:
        return
def tableupdate(table, value, should, where, add=False):
    try:
        conn = auth()
        with conn.cursor() as cursor:
            query = f"UPDATE {table} SET {value} = '{should}' WHERE {where}"
            if add:
                query = f"UPDATE {table} SET {value} = ({should}) WHERE {where}"
            cursor.execute(query)
            conn.commit()
    except:
        return
