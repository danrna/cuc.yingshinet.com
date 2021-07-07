import pymysql

data=[['永安行', '38.66', '43.99%'],
      ['秦港股份', '3.71', '10.09%'],
      ['中船科技', '18.54', '10.03%']]

# pymysql.connect(数据库url,用户名,密码,数据库名 )
db = pymysql.connect("localhost", "root", "123456", "SpiderDB", charset = 'utf8')
cursor = db.cursor()
try:
    for d in data:
        cursor.execute("INSERT INTO stock(name,price,rise) VALUES(%s,%s,%s)", (d[0], d[1], d[2]))
        print("ok")
        db.commit()
except:
    db.rollback()
db.close()
