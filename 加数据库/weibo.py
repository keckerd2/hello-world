import re

count = 0
pattern = re.compile(r'(\S+)\s+(\S+)\s*?')
fd = open('D:\\hack\\社工库\\weibo.com_12160\\weibo.com_12160_py.txt','a+')
fs = open('D:\\hack\\社工库\\weibo.com_12160\\weibo.com_12160.dbh','r',encoding='gb18030',errors='ignore')
lines = fs.readlines()
for line in lines:
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
