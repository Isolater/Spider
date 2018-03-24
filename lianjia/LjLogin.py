# -*- coding: utf-8 -*-
import urllib.request, urllib.parse
import json
import re
import zlib
import http.cookiejar


# 获取Cookiejar对象
#cookie = http.cookiejar.CookieJar()
# 自定义opener
#opener = urllib.request.build_opener(cookie)
#urllib.request.install_opener(opener)

main_url = 'http://sh.lianjia.com/'
auth_url = 'http://upassport.lianjia.com/login'
chengjiao_url = 'http://sh.lianjia.com/chengjiao/'


headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'passport.lianjia.com',
    'Pragma': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'
}


# req = urllib.request.Request(main_url)
# opener.open(req)
#
# req = urllib.request.Request(auth_url, headers)
# result = opener.open(req)


# 获取cookie



# data
data = {
    'username': '18166038384',
    'password': 'Lun950221',
    'execution': 'e1s1',
    '_evevtId': 'submit',
    'lt': '',
}
post_data = urllib.parse.urlencode(data)
post_data = post_data.encode('utf-8')

headers={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'passport.lianjia.com',
    'Origin': 'https://passport.lianjia.com',
    'Pragma': 'no-cache',
    'Referer': 'https://sh.lianjia.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
    'Upgrade-Insecure-Requests': '1',
    'X-Requested-With': 'XMLHttpRequest',
}

req = urllib.request.Request(auth_url, post_data, headers)
res = urllib.request.urlopen(req)
html = res.read()
# result = opener.open(req)
print(html)