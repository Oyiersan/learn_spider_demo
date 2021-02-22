import requests

# https://mp.weixin.qq.com/s?__biz=MzU2ODYzNTkwMg==&mid=2247484251&idx=1&sn=b10a5aedb633a051178fac8a1a800542&scene=19#wechat_redirect
PROXY_POOL_URL = 'http://localhost:55555/random'


def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            print(response.text)
            return response.text
    except ConnectionError:
        return None
