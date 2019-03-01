#coding=utf8
import requests
import itchat
from itchat.content import TEXT

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : '',    #这里自行输入key
        'info'   : msg,
        'userid' : '408451',     #这是我的账号
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return "A Exception Occurred!"    


@itchat.msg_register(TEXT, isFriendChat=True, isGroupChat=False, isMpChat=False)
def tuling_reply(msg):
    defaultReply = 'I received: ' + msg['Text']  #一个默认回复
    reply = get_response(msg['Text'])  
    return reply or defaultReply

itchat.auto_login(True)
itchat.run()
