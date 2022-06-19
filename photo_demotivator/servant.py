import random
from simpledemotivators import Demotivator
import datetime
import sqlite3
import re

date_base = sqlite3.connect("DiscordBase.sqlite3")
cursor = date_base.cursor()


def photo_change(arguments, now):
    """Демотиватор"""
    today = datetime.datetime.today()
    if len(arguments) == 1 and arguments != ['']:
        dem = Demotivator(arguments[0])  # 2 строчки
    elif len(arguments) > 1:
        dem = Demotivator(arguments[0], arguments[1])
    else:
        sqlite_select_query = """SELECT * from messages WHERE links = 2 ORDER BY RANDOM() LIMIT 1;"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchone()
        if random.randint(1, 5) in [1, 2, 4, 5]:
            sqlite_select_query = """SELECT * from messages WHERE links = 2 ORDER BY RANDOM() LIMIT 1;"""
            cursor.execute(sqlite_select_query)
            records2 = cursor.fetchone()
            dem = Demotivator(str(records[1]), str(records2[1]))
        else:
            dem = Demotivator(str(records[1]))
    v = 'photo_demotivator\\' + today.strftime("%Y-%m-%d-%H.%M.%S").replace('.', '-') + '.jpeg'
    dem.create(now, result_filename=v)
    return v


def looking_for_a_link():
    """Ищет ссылку на фотографию, чтобы подставить в демотиватора"""
    cursor.execute("""SELECT COUNT(*) FROM messages""")
    records = cursor.fetchone()
    for i in range(records[0]):

        sqlite_select_query = """SELECT * from messages WHERE links = 1 ORDER BY RANDOM() LIMIT 1;"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchone()

        if re.findall(r'(https?://[^\s]+.png|.jpeg|.jpg)', str(records[1])):
            return str(records[1])
