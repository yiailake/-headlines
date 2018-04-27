# coding=utf8
import requests
from bs4 import BeautifulSoup
import re
import demjson

url = 'https://ssr.tips/46.html#respond'
regex = r"：[\w].+"


headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept - Encoding':'gzip, deflate, br',
               'Accept-Language':'zh-CN,zh;q=0.9',
               'Connection':'Keep-Alive',
               'Cache-Control':'max-age=0',
               'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

cookies = dict(__cfduid='dc5dfb6b331e735cca612ada5cb449c5c1523511143',
               _ga='GA1.2.1620011021.1523511016',
               _gat_gtag_UA_109857345_1='1',
               _gid='GA1.2.85495937.1524538297',
               comment_author_7aaef9ab848668e85607fa468edb77fd='nicheng',
               comment_author_email_7aaef9ab848668e85607fa468edb77fd='nicheng%40qq.com')

r = requests.get(url, cookies=cookies, headers=headers)
#print(r.text)
bs=BeautifulSoup(r.text, "lxml")
p = bs.find("p", {"class":"secret-password"})
#print(p)
matches = re.finditer(regex, str(p))
ls = []
for matchNum, match in enumerate(matches):
    if matchNum > 1:
        result = str(match.group()).replace("：","").replace("<br/>","")
        ls.append(result)
    else:
        print(str(match.group()).replace("：","").replace("<br/>",""))
addr = ls[0].split("--------------")
del addr[2]
del ls[0]
info = addr+ls
print(info)

#f = open('C:\TDDownload\gui-config.json', 'r+', encoding='UTF-8')
data = '''
{"configs":[{"remarks":"","id":"A3C54F835637ABD1F0919DA975726271","server":"serve0","server_port":8388,"server_udp_port":0,"password":"0","method":"chacha20","protocol":"auth_chain_a","protocolparam":"","obfs":"tls1.2_ticket_auth","obfsparam":"","remarks_base64":"","group":"ss.tips","enable":true,"udp_over_tcp":false},{"remarks":"","id":"CBDC1625041120A85586D1EE0F905166","server":"server1","server_port":8388,"server_udp_port":0,"password":"0","method":"chacha20","protocol":"auth_chain_a","protocolparam":"","obfs":"tls1.2_ticket_auth","obfsparam":"","remarks_base64":"","group":"ss.tips","enable":true,"udp_over_tcp":false}],"index":0,"random":true,"sysProxyMode":1,"shareOverLan":false,"localPort":1080,"localAuthPassword":"-iT-HKUKP0mAVHboeb4O","dnsServer":"","reconnectTimes":2,"randomAlgorithm":3,"randomInGroup":false,"TTL":0,"connectTimeout":5,"proxyRuleMode":2,"proxyEnable":false,"pacDirectGoProxy":false,"proxyType":0,"proxyHost":null,"proxyPort":0,"proxyAuthUser":null,"proxyAuthPass":null,"proxyUserAgent":null,"authUser":null,"authPass":null,"autoBan":false,"sameHostForSameTarget":false,"keepVisitTime":180,"isHideTips":false,"nodeFeedAutoUpdate":true,"serverSubscribes":[],"token":{},"portMap":{}}
'''
text = demjson.decode(data)

text["configs"][0]["server"] = "{0}".format(info[0])
text["configs"][0]["server_port"] = int(info[2])
text["configs"][0]["password"] = "{0}".format(info[3])

text["configs"][1]["server"] = "{0}".format(info[1])
text["configs"][1]["server_port"] = int(info[2])
text["configs"][1]["password"] = "{0}".format(info[3])
print(demjson.encode(text))
f = open('D:/gui-config.json', 'w', encoding='UTF-8')
f.write(demjson.encode(text))
f.close()


    
    
   

