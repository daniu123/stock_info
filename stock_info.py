import requests
import time
import os


class Stock(object):
    def __init__(self, stock_num):
        self.stock_num = stock_num

    def info(self):
        link = "https://hq.sinajs.cn/list=" + self.stock_num
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}
        r = requests.get(link, headers=headers)
        r.encoding = 'GBK'
        infos = r.text.split(',')
        stock_name = infos[0].split('"')[-1]
        now_price = infos[3]
        yesterday_price = infos[2]
        ratio = 100*(float(now_price)-float(yesterday_price))/float(yesterday_price)
        print(stock_name, now_price, str(round(ratio, 2))+"%")


if __name__ == '__main__':

    dp = Stock("sh000001")
    sz = Stock("sz399001")
    try:
        while(True):
            dp.info()
            sz.info()
            time.sleep(2)
            os.system("clear")
    except KeyboardInterrupt:
        pass
