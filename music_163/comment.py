import requests
from bs4 import BeautifulSoup
import time
import musics


class Comment(object):
    headers = {
        'Host': 'music.163.com',
        'Connection': 'keep-alive',
        'Content-Length': '484',
        'Cache-Control': 'max-age=0',
        'Origin': 'http://music.163.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'DNT': '1',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
        'Cookie': 'JSESSIONID-WYYY=b66d89ed74ae9e94ead89b16e475556e763dd34f95e6ca357d06830a210abc7b685e82318b9d1d5b52ac4f4b9a55024c7a34024fddaee852404ed410933db994dcc0e398f61e670bfeea81105cbe098294e39ac566e1d5aa7232df741870ba1fe96e5cede8372ca587275d35c1a5d1b23a11e274a4c249afba03e20fa2dafb7a16eebdf6%3A1476373826753; _iuqxldmzr_=25; _ntes_nnid=7fa73e96706f26f3ada99abba6c4a6b2,1476372027128; _ntes_nuid=7fa73e96706f26f3ada99abba6c4a6b2; __utma=94650624.748605760.1476372027.1476372027.1476372027.1; __utmb=94650624.4.10.1476372027; __utmc=94650624; __utmz=94650624.1476372027.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    }

    params = {
        'csrf_token': ''
    }

    data = {
        'params': 'EtEneBmp8Wu4M6gQEWAZimh2rH/ayaxGdzeyZK016ZMtfzuahuFgVcjt5wLymeo9imR1YytAB3szy0JJ+8giVVmh1ajGqhqJImYV2H/ZHAqrk/hZtCRArwZd+B+yRdFKL8aUmqe0Yo85KyvZAUBgafOsaX+JvYa7l0U+Dt7MOhFharmDWb6Pc7D88VYrQNvx',
        'encSecKey': 'a4f00d4e9d747b787cb0226bfafa9d783f89ebf7c57fbcaa3ecfb9cc38c467b6a1c4e4cb40eff85d9b8cb04a76fe7fa03aaaa11375325ccff744c5db12d400fa780a09ecb5572241947f4505199f69796724137d0fd3eb64d93895f4bccc8122b78d26f7db5540dde7734ecbb2dc952fdd9fb4ba99c5f2720c8890e3c70c92cd'
    }

    proxies = {'http': 'http://127.0.0.1:10800'}

    def get_comments(self, music_id):
        self.headers['Referer'] = 'http://music.163.com/playlist?id=' + str(music_id)
        r = requests.post('http://music.163.com/weapi/v1/resource/comments/R_SO_4_' + str(music_id),
                            headers=self.headers, params=self.params, data=self.data, proxies=self.proxies)

        return r.json()


if __name__ == '__main__':
    my_comment = Comment
    music = musics.all_music
    for key, value in music.items():
        try:
            comments = my_comment.get_comments(key[0])
            if comments['total'] > 0:
                print(comments)
        except Exception as e:
            print(str(value) + ':' + str(e))
            time.sleep(2)


