import sqlite3

conn = sqlite3.connect("Address.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE if exists address")

cursor.execute("CREATE TABLE if not exists address(Id serial, Name text, addr text)")
cursor.execute("INSERT INTO address VALUES(1, 'Dominica', 'Seoul')")
cursor.execute("INSERT INTO address VALUES(2, 'RuRi', 'Toronto')")
cursor.execute("INSERT INTO address VALUES(3, 'Ruo', 'alberta')")

conn.commit()

cursor.execute("SELECT * FROM address")

for row in cursor:
	print ("%s 의 주소는 %s 입니다. " %(row[1], row[2]))
	
conn.close()
