import mysql.connector as s
conn=s.connect(host='localhost',user='root',passwd='mehul1995',database='bdays')
cursor=conn.cursor()
#cursor.execute('select * from list')

#f=cursor.fetchall()

cursor.execute('drop table lol')
