
#------------------------------------

#生成100个key，每个key长度为15位

#------------------------------------

import string
import random

def create_string(len):
    str=""
    for i in range(len):
        #所有大写字母和数字随机
        str+=random.choice(string.ascii_uppercase + string.digits)
    return str
    

def create_key(count,len):
    
    for j in range(count):
        return create_string(len)

if __name__=="__main__":
    #创建100个key,每个key长度为15位
    print(create_key(100,15))
