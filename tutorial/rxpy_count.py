'''
从文件中读取所有QQ号，并对QQ号去重统计
'''
from rx import Observable, Observer

def read_lines(file_name):
    file = open(file_name)

    return Observable.from_(file) \
        .map(lambda l: l.strip()) \
        .filter(lambda l: l != "").publish()


source = read_lines("qq.txt")
source.distinct().subscribe(on_next= lambda s: print(s),
       on_completed= lambda: print("file data source Done!\n")
   )
source.distinct().count().subscribe(on_next= lambda s: print("count=", s),
       on_completed= lambda: print("file data source count Done!\n")
   )
source.connect()