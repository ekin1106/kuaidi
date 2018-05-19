import os,sys
import requests
from urllib.parse import urlencode

class kuaidi():
    def __init__(self):
        self.base_url = 'http://www.kuaidi100.com/query?'
        num_post = input(u'快递号码:')
        self.url = 'http://www.kuaidi100.com/autonumber/autoComNum?resultv2=1&text={}'.format(num_post)

    def check_post(self):
        req = requests.session()
        web = req.get(self.url).json()
        check_num = len(web['auto'])
        pos_url = []
        if check_num != 0:
            for n in range(check_num):
                quote = {'type':web['auto'][n]['comCode'],
                         'postid':web['num']}
                check_url = self.base_url+urlencode(quote)
                pos_url.append(check_url)
        return pos_url
    def detail(self,url):
        req = requests.session()
        web = req.get(url).json()
        return web

if __name__ == '__main__':
    kd = kuaidi()
    i = kd.check_post()[0]
    data = kd.detail(i)['data']
    if kd.detail(i)['status'] == '200':
        for detailed in data:
            print('时间:{}'.format(detailed['time']))
            print('======================================')
            print('包裹所在:{}'.format(detailed['context']))
