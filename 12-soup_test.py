from bs4 import  BeautifulSoup

#打开本地文件，生成对象
soup = BeautifulSoup(open('soup_test.html',encoding='utf-8'),'lxml')
# print(soup.a['href']) #通过标签名查找，只能找到第一个标签。这里是a标签的href

#获取所有属性attrs
print(soup.a.attrs)

#获取文本内容，下面三个差不多
print(soup.a.text)
print(soup.a.string) #只有文本的时候才能获取，还有标签的话返回none
print(soup.a.get_text())

# print(soup.find('a')) #与soup.a同，找第一个
print(soup.find('a',title = 'qing')) #带内容找

tang = soup.find('div', class_='tang') #在tang标签下找
print(tang.find('a'))

print(soup.find_all('a'))   #找所有，
print(soup.find_all(['a','b'])) #可以传多个参数进来，
print(soup.find_all('a', limit=2))  #最多找2个

####  SELECT 根据选择器选择指定内容
#返回的都是列表
#CLASS用 .
print(soup.select('.tang > ul > li > a')[1])
#ID用 #
print(soup.select('#du')[0].text)
print(soup.select('#du')[0]['href'])

div = soup.find('div', class_='tang')
print(div.select('#du'))


