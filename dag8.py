from DBUtils import select

sql = "select * from t_employees where sal > %s"
param = [800]

data: object = select(sql,param,mode="many",size=1)

for i in data:
    print(i)



