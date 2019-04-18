import re
from bs4 import BeautifulSoup

class HTMLParser(object):

    def parser(self, page_url, html_content):
        '''
        用于解析网页内容，抽取 URL 和数据
        :param page_url: 下载页面的 URL
        :param html_content: 下载的网页内容
        :return: 返回 URL 和数据
        '''
        if page_url is None or html_content is None:
            return
        soup = BeautifulSoup(html_content, 'html.parser')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        '''
        抽取新的 URL 集合
        :param page_url:下载页面的 URL
        :param soup: soup 数据
        :return: 返回新的 URL 集合
        '''
        new_urls = set()
        for link in range(668000, 668009):
            # 添加新的url
            new_url = "https://www.jb51.net/books/"+str(link)+".html"
            new_urls.add(new_url)
            print(new_urls)
        return new_urls

    def _get_new_data(self, page_url, soup):
        '''
        抽取有效数据
        :param page_url:下载页面的 url
        :param soup: soup 数据
        :return: 返回有效数据
        '''
        data = {}
        data['url'] = page_url
        data['title'] = ''
        data['pub_time'] = ''
        data['baidu_pan'] = ''
        if soup.find('dt', class_='new2') is not None:
            title = soup.find('dt', class_='new2').find('h1')
            data['title'] = title.get_text()
        if soup.find('span', class_='pub-time') is not None:
            pub_time = soup.find('span', class_='pub-time')
            data['pub_time'] = pub_time.get_text()
        if soup.find('li', class_='baidu') is not None:
            baidu_pan = soup.find('li', class_='baidu').find('a')
            data['baidu_pan'] = baidu_pan.get('href')
        return data