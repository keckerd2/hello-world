#这个库密码文件有问题，全是乱码
import re

count = 0
pattern = re.compile(r',')
pattern2 = re.compile(r'"|\'')

fs = open('D:\\hack\\社工库\\【社工库论坛】集合泄露的明文密码\\passwd_uniq.txt','r',encoding='utf-8')
# fd = open('D:\\hack\\社工库\\2000W酒店\\hotel-A.txt','w',encoding='utf-8')

while True:
    line = fs.readline()
    print(line)
# for line in lines:
#     try:
#         count = count + 1
#         print(line.decode('utf8'))
#         print(line.decode('utf16'))
#         # ret = pattern.findall(line)
#         # if pattern2.findall(line):
#         #     line = re.sub(pattern2,'yinhao',line)
#         # # print(len(ret))
#         # if len(ret) == 32:
#         #     fd.write(line)
#         if count % 100000 == 0:
#             print('已加到%d行' % count)
#         # print(text)
#     except Exception as e:
#             # db.rollback()
#             print('第'+str(count)+'行')
#             print(e)
print('已完成%d行' % count)
# fd.close()
fs.close()
