import requests
from bs4 import BeautifulSoup

class Content:
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

    def print(self):
        print('URL: {}'.format(self.url))
        print('TITLE: {}'.format(self.title))
        print('BODY:\n{}'.format(self.body))

class Website:
    def __init__(self, name, url, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.titleTag = titleTag
        self.bodyTag = bodyTag

class Crawler:

    def getPage(self, url):
        headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept - Encoding':'gzip, deflate, br',
               'Accept-Language':'zh-CN,zh;q=0.9',
               'Connection':'Keep-Alive',
               'Cache-Control':'max-age=0',
               'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
        try:
            req = requests.get(url, headers=headers)
        except requests.exceptions.RequestException as e:
            print(e)
            return None
        return BeautifulSoup(req.text, 'lxml')

    def safeGet(self, pageObj, selector):
        selectedElems = pageObj.select(selector)
        if selectedElems is not None and len(selectedElems) > 0:
            return '\n'.join([elem.get_text() for elem in selectedElems])
        return ''

    def parse(self, site, url):
        bs = self.getPage(url)
        if bs is not None:
            title = self.safeGet(bs, site.titleTag)
            body = self.safeGet(bs, site.bodyTag)
            if title != '' and body != '':
                content = Content(url, title, body)
                content.print()


if __name__ == '__main__':
    crawler = Crawler()
    siteData = [
        ['O\'Reilly Media', 'http://oreilly.com','h1', 'section#product-description'],
        ['Reuters', 'http://reuters.com', 'h1','div.body_1gnLA'],
        ['Brookings', 'http://www.brookings.edu','h1', 'div.post-body.post-body-enhanced'],
        ['Tuicool', 'http://www.tuicool.com','h1', 'div.article_body']
    ]
    websites = []
    for row in siteData:
        websites.append(Website(row[0], row[1], row[2], row[3]))
    
    crawler.parse(websites[0], 'http://shop.oreilly.com/product/0636920028154.do')
    #crawler.parse(websites[1], 'https://www.reuters.com/article/us-usa-epa-pruitt-idUSKBN19W2D0')
    #crawler.parse(websites[2], 'https://www.brookings.edu/blog/techtank/2016/03/01/idea-to-retire-old-methods-of-policy-education/')
    crawler.parse(websites[3], 'https://www.tuicool.com/articles/euQzQbq')    