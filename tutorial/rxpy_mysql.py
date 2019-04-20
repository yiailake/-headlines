'''
从MySQL数据库中读取用户信息并打印出来
'''
from rx import Observable, Observer
import datetime, pymysql

conn = pymysql.connect('localhost', 'root', 'admin123', 'test')

def get_all_users():
    sql = "SELECT * FROM users"
    cursor = conn.cursor()
    cursor.execute(sql)
    rs = cursor.fetchall()
    return Observable.from_(rs)

get_all_users() \
    .map(lambda r: r[1]) \
    .subscribe(on_next= lambda s:print(s),
        on_completed= lambda: print("db data source Done!\n")
    )    