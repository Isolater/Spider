import requests
from bs4 import BeautifulSoup
# import mysql


group_list = [1001, 1002, 1003, 2001, 2002, 2003, 6001, 6002, 6003, 7001, 7002, 7003, 4001, 4002, 4003]
all_artist = {}


def save_artist(group_id):
    global all_artist
    r = requests.get("http://music.163.com/discover/artist/cat", params={'id': group_id})
    soup = BeautifulSoup(r.content.decode(), 'html.parser')
    body = soup.body

    hot_artists = body.find_all('a', attrs={'class': 'msk'})
    artists = body.find_all('a', attrs={'class': 'nm nm-icn f-thide s-fc0'})

    for artist in hot_artists:
        artist_id = artist['href'].replace('/artist?id=', '').strip()
        artist_name = artist['title'].replace('的音乐', '')
        try:
            all_artist[artist_id] = artist_name
        except Exception as e:
            print(e)  # 打印错误信息

    for artist in artists:
        artist_id = artist['href'].replace('/artist?id=', '').strip()
        artist_name = artist['title'].replace('的音乐', '')
        try:
            all_artist[artist_id] = artist_name
        except Exception as e:
            print(e)  # 打印错误信息


for i in group_list:
    save_artist(i)
