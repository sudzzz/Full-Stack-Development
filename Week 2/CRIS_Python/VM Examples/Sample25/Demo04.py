import MySQLdb

conn = MySQLdb.connect(host="localhost",
                           user="root",
                           passwd="mysql@python",
                           db="pythondb")
c = conn.cursor()
qr="select * from employee"
c.execute(qr)
data=c.fetchall()

for f in data:
    print(f)
