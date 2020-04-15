

# ------------------------------------

# 生成100个key，每个key长度为15位
# 并插入数据库
# ------------------------------------

import string
import random
import psycopg2

def create_string(len):
    str =""
    for i in range(len):
        # 所有大写字母和数字随机
        str+=random.choice(string.ascii_uppercase + string.digits)
    return str




if __name__=="__main__":
    #链接数据库
    conn = psycopg2.connect(database="my_databse", user="user", password="Aa123456",
                            host="127.0.0.1", port="5432")
    # 创建指针对象
    cur = conn.cursor()
    # 创建100个key,每个key长度为15位
    for j in range(100):
        cur.execute("insert into key_table(key) values ('%s');" % str(create_string(15)))
        conn.commit()
    
    #关闭指针对象
    cur.close()
    #关闭链接
    conn.close()



