import pymysql.cursors

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    db='test',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor
)

# 保存歌手
def insert_artist(artist_id, artist_name):
    with connection.cursor() as cursor:
        sql = "INSERT INTO 'artists' ('ARTIST_ID', 'ARTIST_NAME') VALUES (%s, %s)"
        cursor.execute(sql, (artist_id, artist_name))
    connection.commit()


# 保存专辑
def insert_album(album_id, artist_id, album_name):
    with connection.cursor() as cursor:
        sql = "INSERT INTO album ('ALBUM_ID', 'ARTIST_ID', 'ALBUM_NAME') VALUES(%s, %s, %s)"
        cursor.execute(sql, (album_id, artist_id, album_name))
    connection.commit()


# 保存音乐
def insert_music(music_id, album_id, music_name):
    with connection.cursor() as cursor:
        sql = "INSERT INTO music ('MUSIC_ID', 'ALBUM_ID', 'MUSIC_NAME') VALUES(%s, %s, %s)"
        cursor.execute(sql, (music_id, album_id, music_name))
    connection.commit()


# 保存评论
def insert_comment(music_id, comments, detail):
    with connection.cursor() as cursor:
        sql = "INSERT INTO comment ('MUSIC_ID', 'COMMENTS', 'DETAIL') VALUES(%s, %s, %S)"
        cursor.execute(sql, (music_id, comments, detail))
    connection.commit()
