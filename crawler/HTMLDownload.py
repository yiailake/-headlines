import requests

class HTMLDownload(object):
    def download(self, url):
        if url is None:
            return
        s = requests.Session()
        s.headers['User-Agent'] = ''
        res = s.get(url)
        # 判断是否正常获取
        if res.status_code == 200:
            res.encoding = 'utf-8'
            res = res.text
            return res
        return None
