import requests

# 非 python 的内置库
# pip install requests
# https://mp.weixin.qq.com/s/dYtF8ydJtqub0QkK1cGVjA

r = requests.get('https://api.github.com/events')

print(r.json())


