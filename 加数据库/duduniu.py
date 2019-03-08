# import pymysql
import re

# 打开数据库连接
# db = pymysql.connect("localhost","root","","csdn" )
# 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()

count = 0
pattern = re.compile(r'(\S+)\s+(\S+)\s+(\S+)\s+')
fd = open('D:\\hack\\社工库\\嘟嘟牛\\d-REYE_txt','a+')
pathtxt = 'D:\\hack\\社工库\\嘟嘟牛\\d-REYE_txt.'
for i in range(16):
    fs = open('D:\\hack\\社工库\\嘟嘟牛\\d-REYE_txt.'+str(i+2),'r',encoding='gbk',errors='ignore')
    lines = fs.readlines()
    for line in lines:
        try:
            count = count + 1
            ret = pattern.findall(line)
            userid = ret[0][0]
            name = ret[0][1]
            password = ret[0][2]
            text = userid+','+name+','+password
            fd.write(text+'\n')
            if count % 100000 == 0:
                print('已加到%d行' % count)
            # print(text)
        except Exception as e:
                # db.rollback()
                print('第'+str(count)+'行')
                print(e)
    print('已完成%d行' % count)
    fs.close()
fd.close()

# with open('D:\\hack\\社工库\\人人网500W_16610\\xh-2.txt','r',encoding='gb18030',errors='ignore') as f:
# # with open('D:\hack\社工库\weibo.com_12160\weibo.com_12160.dbh','r') as f:
#     lines = f.readlines()
#     for line in lines[992030:]:
#         count = count + 1
#         ret = pattern.findall(line)
#         name = ret[0][0]
#         password = ret[0][1]
#         sql = "insert into renren values ('','"+name+"','"+password+"');"
#         try:
#             cursor.execute(sql)
#             # db.commit()
#         except Exception as e:
#             db.rollback()
#             print('第'+str(count)+'行',sql)
#             print(e)
#         # print(name,password)
#         if count % 10000 == 0:
#             print('已加到%d行' % count)
#     db.commit()
#     print('已完成%d行' % count)
#
#
#
# db.close()
