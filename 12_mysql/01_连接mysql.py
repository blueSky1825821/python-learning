"""
连接mysql



"""
from pymysql import connections
#获取连接
conn = connections.Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    database="test",
    charset="utf8",
    autocommit=False#非自动提交
)
# 打印mysql数据库软件信息
conn.get_server_info()

#获取游标对象
cursor = conn.cursor()
conn.select_db("test")
#执行sql
cursor.execute("select * from user")
#获取结果集
fetchall: tuple = cursor.fetchall()
for r in fetchall:
    print(r)
#更改需要确认
# conn.commit()
# 关闭连接
conn.close()
