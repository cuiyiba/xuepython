'''
 1.联网安装pymysql
        pip install pymysql
    2.导入pymysql
    3.连接数据库
    4.创建控制台
    5.准备一条语句
        增，删，改：
            提交
        查询：
            提取数据
            fetchone()
            fetchall()
            fetchmany(size)

    6.提交数据到数据库
    7.关闭各项资源
import pymysql

host = "localhost"
user = "root"
password = ""
database = "cuiyiba"


# 增，删，改
def update(sql, param):
    con = pymysql.connect (host=host, user=user, password=password, database=database)

    cursor = con.cursor ()

    cursor.execute (sql, param)

    con.commit ()

    cursor.close ()
    con.close ()


# 查询
def select(sql, param, mode="many", size=1):
    con = pymysql.connect (host=host, user=user, password=password, database=database)

    cursor = con.cursor ()

    cursor.execute (sql, param)
    if mode == "all":
        return cursor.fetchall ()
    elif mode == "one":
        return cursor.fetchone ()
    elif mode == "many":
        return cursor.fetchmany (size)

    con.commit ()

    cursor.close ()
    con.close ()

'''
# 2.导入pymysql
import pymysql

# 3.连接数据库
host = "localhost"
user = "root"
password = ""
database = "cuiyiba"



# 增 删 改
def update(sql, param):
    # 链接数据库
    con = pymysql.connect (host=host, user=user, password=password, database=database)

    # 创建控制台
    cursor = con.cursor ()
    # 执行sql
    cursor.execute (sql, param)
    # 提交
    con.commit ()
    # 关闭控制台
    cursor.close ()
    # 关闭链接
    con.close ()
    # 查询


def select(sql, param, mode="many", size=1):
    # 链接数据库
    con = pymysql.connect (host=host, user=user, password=password, database=database)

    # 创建控制台
    cursor = con.cursor ()
    # 执行sql
    cursor.execute (sql, param)
    # 进行判断
    if mode == "one":
        return cursor.fetchone ()
    elif mode == "all":
        return cursor.fetchall ()
    elif mode == "many":
        return cursor.fetchmany (size)
    else:
        print ("参数有误")
    # 提交
    con.commit ()
    # 关闭控制台
    cursor.close ()
    # 关闭链接
    con.close ()
