import MySQLdb

def connection():
    conn = MySQLdb.connect(host="localhost",
                           user="root",
                           passwd="mysql@python",
                           db="pythondb")
    c = conn.cursor()

    return c, conn

connection()
