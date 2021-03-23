import pymysql
import requests

config = {
    'host': '192.168.0.184',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'database': 'test_dy',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.Cursor,
}

db = pymysql.connect(**config)

# 接着我们获取 cursor 来操作我们的 avIdol 这个数据库
cursor = db.cursor()

# 比如我们来创建一张数据表

# 插入一条记录
sql = "SELECT name, head_portrait FROM sys_user WHERE head_portrait IS NOT NULL"

try:
    cursor.execute(sql)
    data = cursor.fetchall()
    for i in data[:]:
        print(i[0])
        name = i[0]
        req = requests.get(i[1])
        filename = i[0]

        if req.status_code == 200:
            open('E:\\头像\\'+name+'.png', 'wb').write(req.content)
            print("done")

    # db.commit()

except:
    # 回滚
    db.rollback()

cursor.close()
# 最后我们关闭这个数据库的连接
db.close()