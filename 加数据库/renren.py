# import pymysql
import re

# 打开数据库连接
# db = pymysql.connect("localhost","root","","csdn" )
# 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()

count = 992030
pattern = re.compile(r'(\S+)\s+(\S+)\s*?')
fd = open('D:\\hack\\社工库\\人人网500W_16610\\xh-2-py.txt','a+')
fs = open('D:\\hack\\社工库\\人人网500W_16610\\xh-2.txt','r',encoding='gb18030',errors='ignore')
lines = fs.readlines()
for line in lines[992030:]:
    try:
        count = count + 1
        ret = pattern.findall(line)
        name = ret[0][0]
        password = ret[0][1]
        text = name+','+password
        fd.write(text+'\n')
        if count % 100000 == 0:
            print('已加到%d行' % count)
        # print(text)
    except Exception as e:
            # db.rollback()
            print('第'+str(count)+'行')
            print(e)
print('已完成%d行' % count)
fd.close()
fs.close()
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
