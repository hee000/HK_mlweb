from flask import json
import pymysql
import pymysql
from PIL import Image
import base64
from io import BytesIO
import time
import json


flask_db = pymysql.connect(
    user='root', 
    passwd='2800512', 
    host='localhost', 
    db='flask', 
    charset='utf8'
)

cursor = flask_db.cursor(pymysql.cursors.DictCursor)

def info(email):
    sql = f"SELECT id, email, password FROM `users` WHERE email = '{email}';"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def insert(email, password):
    sql = f'''INSERT INTO `users` (email, password) 
        VALUES ('{email}', '{password}');'''
    cursor.execute(sql)
    flask_db.commit()

def img(name, imgblob):
    sql = "INSERT INTO Images (name, imageData) VALUES (%s, %s)"

    cursor.execute(sql,(name, imgblob))
    flask_db.commit()    

def testinfo():
    sql = f"SELECT id, email, password FROM `users`;"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result   

def test():
    # id, pw를 user에서 고윳값을 찾아 고윳값 번호의 테이블로 이동, 테이블에서 이미지 name을 뽑아 리턴      
    sql = "SELECT name, imageData FROM Images"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


# print(result)

## 이미지 복원
# sql = f"SELECT imageData FROM Images "
# cursor.execute(sql)
# image = cursor.fetchall()
# for i in image:
#     img = base64.decodestring(i['imageData'])
#     get_image = Image.open(BytesIO(img))
#     get_image.show()

## 이미지 이름
# sql = "SELECT name FROM Images"
# cursor.execute(sql)
# result = cursor.fetchall()
# print(type(result))
# print(result[0])

result = test()
image = result[0]['imageData']

img = base64.decodestring(image)

a = Image.open(BytesIO(img))
a.show()
# a.show()

### 테이블 크기 용량
# sql = "SELECT table_name, table_rows, round(data_length/(1024*1024),2) as 'DATA_SIZE(MB)', round(index_length/(1024*1024),2) as 'INDEX_SIZE(MB)' FROM information_schema.TABLES WHERE table_schema = 'flask' AND table_name='Images';"
# cursor.execute(sql)
# result = cursor.fetchall()
# result = float(result[0]['DATA_SIZE(MB)'])
# print(type(result))
# print(type(image))
# print(image[0].keys())



# with open("/Users/cho/Desktop/desktop2/연구원등록/신분증 사본.jpg", "rb") as img2:
#     img = img2.read()


# img = base64.b64encode(img)
# # img = img.decode("UTF-8")
# print(type(img))
# get_image = Image.open(img)
# get_image.show()
# # get_image = Image.open(BytesIO(img))
# # get_image = img['image']
# # get_image.show()
# # # print(type(img))
# # # BytesIO(img)
# # CREATE DATABASE flask;

# # USE flask;

# CREATE TABLE users(
#     id INT NOT NULL AUTO_INCREMENT, # AUTO_INCREMENT: 해당 칼럼의 값이 자동으로 1씩 증가된다.
#     email VARCHAR(255) NOT NULL,
#     password VARCHAR(255) NOT NULL,
#     created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     PRIMARY KEY (id), # 고유키로 설정할 컬럼
#     UNIQUE KEY email (email) # 해당 컬럼의 값이 중복되는 값이 존재하면 안됨
# );

# CREATE TABLE Images(
#     id INT NOT NULL AUTO_INCREMENT, # AUTO_INCREMENT: 해당 칼럼의 값이 자동으로 1씩 증가된다.
#     imageData LONGBLOB,
#     PRIMARY KEY (id)
# );



# create table test3 (
#     num int(10) not null,
#     name varchar(20) not null
#     )max_rows=4000000000
# ;