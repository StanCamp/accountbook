import pymssql


def connection():
    serverName = '127.0.0.1'  # 目的主机ip地址
    userName = 'sa'  # SQL Server身份账号
    passWord = '2015815yin'  # SQL Server身份密码
    dbName = 'python'  # 对应数据库名称
    db = pymssql.connect(serverName, userName, passWord, dbName)  # SQL Server身份验证建立连接
    if db:
        print('连接成功!')
        return db
    else:
        print('连接失败')
        return None
