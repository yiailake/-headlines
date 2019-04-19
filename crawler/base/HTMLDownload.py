import requests
from requests.adapters import HTTPAdapter

class HTMLDownload(object):
    def download(self, url):
        if url is None:
            return
        s = requests.Session()
        s.mount('http://', HTTPAdapter(max_retries=3))
        s.mount('https://', HTTPAdapter(max_retries=3))
        s.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'
        try:
            res = s.get(url, timeout=5)
        except requests.exceptions.RequestException as e:
            print(e)
        # 判断是否正常获取
        if res.status_code == 200:
            res.encoding = 'gb2312'
            res = res.text
            return res
        return None
