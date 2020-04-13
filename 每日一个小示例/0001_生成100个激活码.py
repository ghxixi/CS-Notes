
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
    import csv
    file=open('d:/key_code.txt','w')
    for j in range(count):
        file.write(create_string(len))
    
    file.close()

if __name__=="__main__":
    #创建100个key,每个key长度为15位
    create_key(100,15)
