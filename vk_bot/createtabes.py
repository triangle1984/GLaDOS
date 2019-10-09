import pymysql
from pymysql.cursors import DictCursor
from contextlib import closing
from vksql import authW
from token import *
conn = auth()
with conn.cursor() as cursor:
    query = "CREATE TABLE IF NOT EXISTS admins (id int)"
    cursor.execute(query)
    query = "CREATE TABLE IF NOT EXISTS ban (id int)"
    cursor.execute(query)
    query = f"CREATE TABLE IF NOT EXISTS {tablechat} (id int)"
    cursor.execute(query)
    query = f"CREATE TABLE IF NOT EXISTS prefix (id int, name varchar(40))"
    cursor.execute(query)
    query = f"CREATE TABLE IF NOT EXISTS smehgen (id int, count int, smeh varchar(40), smehslova varchar(40))"
    cursor.execute(query)
    query = f"CREATE TABLE IF NOT EXISTS prefix (id int, name varchar(40))"
    cursor.execute(query)
    query = f"CREATE TABLE IF NOT EXISTS {chathello} (id int)"
    cursor.execute(query)
    query = f"CREATE TABLE IF NOT EXISTS {chathello} (id int)"
