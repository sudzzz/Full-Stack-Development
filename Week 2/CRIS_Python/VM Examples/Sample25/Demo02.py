from flask import Flask
from flask_mysqldb import MySQL


app=Flask(__name__)
mysql=MySQL(app)

@app.route('/')
def users():
    cur=mysql.connection.cursor()
    cur.execute('''select * frpom mysql.pythondb''')
    rv=cur.fetchall()
    return str(rv)

if(__name__=='__main__'):
    app.run(debug=True)

