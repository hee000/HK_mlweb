import pymysql
# import json
from flask import Flask, jsonify

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

def imginfo(id, pw):
    # id, pw를 user에서 고윳값을 찾아 고윳값 번호의 테이블로 이동, 테이블에서 이미지 name을 뽑아 리턴      
    sql = "SELECT name FROM Images"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def test():
    # id, pw를 user에서 고윳값을 찾아 고윳값 번호의 테이블로 이동, 테이블에서 이미지 name을 뽑아 리턴      
    sql = "SELECT name, imageData FROM Images"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def diskinfo():
    # id, pw를 user에서 고윳값을 찾아 고윳값 번호의 테이블로 이동, 테이블에서 이미지 name을 뽑아 리턴      
    sql = "SELECT table_name, table_rows, round(data_length/(1024*1024),2) as 'DATA_SIZE(MB)', round(index_length/(1024*1024),2) as 'INDEX_SIZE(MB)' FROM information_schema.TABLES WHERE table_schema = 'flask' AND table_name='Images';"
    cursor.execute(sql)
    result = cursor.fetchall()
    result = float(result[0]['DATA_SIZE(MB)'])
    # result = flask.json.jsonify(result)
    # result = json.dumps(result[0])
    return {"usingdisk" : result}



def testinfo():
    sql = f"SELECT id, email, password FROM `users`;"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result






# print(result)


# CREATE DATABASE flask;

# USE flask;

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
#     name VARCHAR(255) NOT NULL,
#     imageData LONGBLOB,
#     PRIMARY KEY (id)
# );