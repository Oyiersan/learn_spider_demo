from urllib import request, parse
import ssl
import urllib.request

# 我们可以使用 ssl 未经验证的上下文
context = ssl._create_unverified_context()

# url = 'https://biihu.cc//account/ajax/login_process/'
url = 'https://id.app.acfun.cn/rest/web/login/signin'
headers = {
    # 假装自己是浏览器
    # 'User-Agent': ' Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
}

dict = {
    'username': '15696922101',
    'password': 'zhjw!75355280',
    'key': '',
    'captcha': ''
}

data = bytes(parse.urlencode(dict), 'utf-8')

req = request.Request(url, data=data, headers=headers, method='POST')

response = request.urlopen(req)
print(response.read().decode('utf-8'))


# response = urllib.request.urlopen('http://www.baidu.com')
# response = urllib.request.Request('http://www.baidu.com')
# print(response.read().decode('utf-8'))
