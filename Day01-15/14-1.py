from time import time
from threading import Thread
import requests

# 继承Thread类创建自定义的线程类


class DownloadHandler(Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open('User/Hao' + filename, 'wb') as f:
            f.write(resp.content)


def main():
    """
    通过requests模块的get函数获取网络资源
    """
    resp = requests.get('http://api.tianapi.com/meinv/?key=APIKey&num=10')
    # 将服务器返回的json格式的数据解析为字典
    data_model = resp.json()
    for mm_dict in data_model['newslist']:
        url = mm_dict['picUrl']
        DownloadHandler(url).start()


if __name__ == "__main__":
    main()
