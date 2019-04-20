'''
获取新浪的美股接口数据，并打印出股票名和价格
'''
from rx import Observable, Observer
from urllib.request import urlopen

def read_request(link):
    f = urlopen(link)

    return Observable.from_(f) \
        .map(lambda s: s.decode("gbk").strip()) 

codes = ["usr_aapl", "usr_fb", "usr_goog", "usr_baba"]
source = Observable.from_(codes)\
    .map(lambda s: "http://hq.sinajs.cn/list={0}".format(s))\
    .flat_map(lambda s: read_request(s)) \
    .map(lambda s: s.split('"')[1]) \
    .filter(lambda l: l != "") \
    .map(lambda s: s.split(","))\
    .map(lambda s: "股票：{0}           价格：{1}".format(s[0], s[1]))

source.subscribe(on_next= lambda s: print(s))
source.count().subscribe(on_next= lambda s: print("count=", s),
      on_completed= lambda: print("network data source Done!\n")
   )                    