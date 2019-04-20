'''
将文章信息列表关联作者名称
'''
from rx import Observable, Observer

articles = [
    {"post_id":1, "author_id":1, "title":"title1"},
    {"post_id":2, "author_id":2, "title":"title2"},
    {"post_id":3, "author_id":2, "title":"title2"}
]
authors = [
    {"author_id":1, "name":"AA"},
    {"author_id":2, "name":"BB"}
]

Observable.from_(articles)\
    .flat_map(
        lambda x: Observable.zip(Observable.just(x),
        Observable.from_(authors).filter(lambda y: y["author_id"]  == x["author_id"]),
        lambda l, r: dict(list(l.items()) + list(r.items())) ))\
    .subscribe(on_next= lambda s: print(s),
        on_completed= lambda: print("group_by Done!\n")
    )