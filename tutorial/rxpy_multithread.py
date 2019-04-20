'''
以多线程的方式，按列表读取新浪接口美股的数据
'''
from rx import Observable, Observer
from rx.concurrency import ThreadPoolScheduler
from threading import current_thread
import multiprocessing, datetime
from urllib.request import urlopen

optimal_thread_count = multiprocessing.cpu_count() + 1
pool_scheduler = ThreadPoolScheduler(optimal_thread_count)

def read_request(link):
    f = urlopen(link)
    return Observable.from_(f) \
        .map(lambda s: s.decode("gbk").strip())

print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))

codes = codes = ["usr_aapl", "usr_fb", "usr_goog", "usr_baba", "usr_ge", "usr_tsla", "usr_atvi", "usr_hpq"]

source = Observable.from_(codes)\
    .map(lambda s: "http://hq.sinajs.cn/list={0}".format(s))\
    .flat_map(lambda s: 
        Observable.just(s).subscribe_on(pool_scheduler).flat_map(lambda t: read_request(t))
    )\
    .map(lambda s: s.split('"')[1]) \
    .filter(lambda l: l != "") \
    .map(lambda s: s.split(","))\
    .map(lambda s: "股票：{0}           价格：{1}".format(s[0], s[1]))

source.subscribe(on_next= lambda i: print("{0} {1}".format(current_thread().name, i)),
            on_error= lambda e: print(e),
            on_completed= lambda: print("PROCESS 1 Done!", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")))

print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))

input("Press any key to exist\n")