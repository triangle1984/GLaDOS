import pymysql
from pymysql.cursors import DictCursor
from contextlib import closing
from loadevn import *
def auth():
    conn = pymysql.connect(host=ip,
                             user=user,
                             password=password,
                             db=db,
                             cursorclass=DictCursor)
    return conn
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
            if one:
                if bool(checktable(table, value, add)):
                    return
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
def tableupdate(table, value, should, where, add=False):
    conn = auth()
    with conn.cursor() as cursor:
        query = f"UPDATE {table} SET {value} = '{should}' WHERE {where}"
        if add:
            query = f"UPDATE {table} SET {value} = ({should}) WHERE {where}"
        cursor.execute(query)
        conn.commit()
