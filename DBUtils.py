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
