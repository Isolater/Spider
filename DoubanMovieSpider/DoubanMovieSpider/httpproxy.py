# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request
import http.client
import csv
ips = {}


def getProxyList(targeturl='http://www.xicidaili.com/nn/'):
    global ips
    countNum = 0
    requestHeader = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/37.36"}

    for page in range(1, 20):
        url = targeturl + str(page)
        request = urllib.request.Request(url,headers=requestHeader)
        html = urllib.request.urlopen(request).read()
        myurl = 'www.baidu.com'
        soup = BeautifulSoup(html, 'html.parser')
        trs = soup.find('table', id='ip_list').find_all('tr')
        for tr in trs[1:]:
            tds = tr.find_all('td')

            unverifyIP = tds[2].text.strip()
            unverifyPORT = tds[3].text.strip()
            try:
                conn = http.client.HTTPConnection(unverifyIP, unverifyPORT, timeout=5.0)
                conn.request(method='GET', url=myurl, headers=requestHeader)
                res = conn.getresponse()  # 说明代理ip有效
                if tds[1].find('img') is None:
                    nation = '未知'
                    locate = '未知'
                else:
                    nation = tds[1].find('img')['alt'].strip()
                    locate = tds[4].text.strip()
                ip = unverifyIP
                port = unverifyPORT
                anony = tds[5].text.strip()
                protocol = tds[6].text.strip()
                speed = tds[7].find('div')['title'].strip()
                time = tds[9].text.strip()
                data = [[nation, ip, port, locate, anony, protocol, speed, time]]
                with open('iplist.csv', 'w', newline='') as f:
                    writer = csv.writer(f)
                    for row in data:
                        writer.writerow(row)
            except:
                pass

            countNum += 1

        return countNum


if __name__ == '__main__':
    proxynum = getProxyList('http://www.xicidaili.com/nn/')
    print('国内高匿数量：' + str(proxynum))
    proxynum = getProxyList('http://www.xicidaili.com/nt/')
    print('国内透明数量：' + str(proxynum))
    proxynum = getProxyList('http://www.xicidaili.com/wn/')
    print('国外高匿数量：' + str(proxynum))
    proxynum = getProxyList('http://www.xicidaili.com/wt/')
    print('国外透明数量：' + str(proxynum))

