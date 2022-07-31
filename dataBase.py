import unit


# 用于查询
def executeQuery(sql):
    db = unit.connection()
    cur = db.cursor()
    try:
        # 执行sql语句
        cur.execute(sql)
        result = cur.fetchall()
        db.commit()
        cur.close()
        return result
    except Exception as e:
        # 出现错误即使回滚数据
        print(e)
        db.rollback()
    db.close()


# 用于增删改查
def executeUpdate(sql):
    db = unit.connection()
    cur = db.cursor()
    try:
        # 执行sql语句
        cur.execute(sql)
        db.commit()
        cur.close()
        db.close()
        return True
    except Exception as er:
        db.rollback()  # 数据回滚
        print("数据修改失败" + (str(er)))
        cur.close()
        db.close()
        return False
