import sqlite3

conn=sqlite3.connect("Stu.db")
cur=conn.cursor()
cur.execute("INSERT INTO `Student` (Sno,Sname,Ssex,Scollege_name,Sbirth) VALUES ('20210119','刘强亮','男','生工学院','2002-01-01 00:00:00.000')")
conn.commit()
conn.close()