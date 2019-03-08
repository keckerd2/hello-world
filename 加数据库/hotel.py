import re

count = 0
pattern = re.compile(r',')
pattern2 = re.compile(r'"|\'')

fd = open('D:\\hack\\社工库\\2000W酒店\\hotel-A.txt','w',encoding='utf-8')
# fs = open('D:\\hack\\社工库\\2000W酒店\\酒店开房数据库-A-0001-200W.csv','r',encoding='gb18030',errors='ignore')
fs = open('D:\\hack\\社工库\\2000W酒店\\酒店开房数据库-A-0001-200W.csv','r',encoding='utf-8',errors='ignore')
# fd.write(u'Name,CardNo,Descriot,CtfTp,CtfId,Gender,Birthday,Address,Zip,Dirty,District1,District2,District3,District4,District5,District6,FirstNm,LastNm,Duty,Mobile,Tel,Fax,EMail,Nation,Taste,Education,Company,CTel,CAddress,CZip,Family,Version,id﻿\n')
lines = fs.readlines()
for line in lines:
    try:
        count = count + 1
        ret = pattern.findall(line)
        if pattern2.findall(line):
            line = re.sub(pattern2,'yinhao',line)
        # print(len(ret))
        if len(ret) == 32:
            fd.write(line)
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
