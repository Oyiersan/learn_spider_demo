
import requests

# https://mp.weixin.qq.com/s?__biz=MzU2ODYzNTkwMg==&mid=2247484267&idx=1&sn=53486a7f41d9f57d14b10b7a21bfbb1e&chksm=fc8bbbfacbfc32ecb6a27b94f11c3902600d5064c3715b89a669c8e5a743e0749a4145a6f364&cur_album_id=1321044729160859650&scene=189#rd

headers = {
    # 假装自己是浏览器
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/73.0.3683.75 Chrome/73.0.3683.75 Safari/537.36',
    # 把你刚刚拿到的Cookie塞进来
    'Cookie': 'eda38d470a662ef3606390ac3b84b86f9; Hm_lvt_f1d3b035c559e31c390733e79e080736=1553503899; biihu__user_login=omvZVatKKSlcXbJGmXXew9BmqediJ4lzNoYGzLQjTR%2Fjw1wOz3o4lIacanmcNncX1PsRne5tXpE9r1sqrkdhAYQrugGVfaBICYp8BAQ7yBKnMpAwicq7pZgQ2pg38ZzFyEZVUvOvFHYj3cChZFEWqQ%3D%3D; Hm_lpvt_f1d3b035c559e31c390733e79e080736=1553505597',
}

session = requests.Session()
response = session.get('https://biihu.cc/people/wistbean%E7%9C%9F%E7%89%B9%E4%B9%88%E5%B8%85', headers=headers)

print(response.text)