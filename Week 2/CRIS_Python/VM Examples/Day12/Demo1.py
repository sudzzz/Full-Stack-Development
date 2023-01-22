import sqlite3

dbobj=sqlite3.connect("June28_Db.db")
qr=dbobj.cursor()

def CreatTable():
    qr.execute("create table "
               "if not exists items"
               "(id integer primary key,"
               "category varchar(20),"
               "name varchar(20),"
               "price number,"
               "qty number)")

    qr.execute("create table "
           "if not exists items_sold"
           "(iid integer primary key "
               "autoincrement,"
               "totalqty number)")

def InsertValues_Items(i,c,n,p,q):
    qr.execute("insert into Items "
               "values(?,?,?,?,?)",(i,c,n,p,q))
    dbobj.commit()

def InsertValues_Items_sold(t):
    qr.execute("insert into Items_sold(totalqty) "
               "values(100)")
    dbobj.commit()

def main():
    CreatTable()
    '''ctr=0
    while(ctr<3):
        id=int(input("Enter id"))
        cat= (input("Enter category"))
        nam= (input("Enter name"))
        pri = int(input("Enter price"))
        qty=int(input("Enter qty"))
        InsertValues_Items(id,cat,nam,pri,qty)
        ctr+=1
    lst=[100,200,300,400,500]

    for l in lst:
        InsertValues_Items_sold(int(l))
'''
    qr.execute("select * from Items")
    for l in qr:
        print(l)
    qr.execute("select * from Items_sold")
    for l in qr:
        print(l)
    print('Lets Display Both Tables Records')
    qr.execute("select * from Items JOIN Items_sold on items.id=items_sold.iid")
    for l in qr:
        print(l)

    print('Lets Display Categories')
    qr.execute("select distinct category from Items")
    for l in qr:
        print(l[0])
    print('Lets Have SubQuery')
    qr.execute("select * from Items left outer join items_sold on items.id=items_sold.iid")
    for l in qr:
        print(l)

    print('Lets subquery')
    qr.execute("select * from Items  where id in (select iid from Items_sold)")
    for l in qr:
        print(l)


    print('Lets subquery')
    qr.execute("select category,count(*) from Items group by category")
    for l in qr:
        print(l)

print(date('now'))
#main()

