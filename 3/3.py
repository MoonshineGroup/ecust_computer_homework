import requests
import re
import sqlite3

url="http://www.wandoujia.com/apps"
response=requests.get(url)
data=response.text
conn=sqlite3.connect("school.db")
sql1='''create table information(name text,link text)'''
conn.execute(sql1)

mydata=re.findall('<a class="cate-link"\s+href="(.+)"\s+title="(.+)">',data)

for item in mydata:
    SQL='''insert into information (name, link) values('%s', '%s')'''%(item[1],item[0])                   
    conn.execute(SQL)
    conn.commit()
conn.close()
