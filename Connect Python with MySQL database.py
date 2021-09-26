import mysql.connector

mydb=mysql.connector.connect(
    host='localhost', 
    user='root', 
    password='*********',  #put your MySQL password
    database='db1')
print(mydb.connection_id)

cur=mydb.cursor()
#To create database
#S="CREATE TABLE book(bookid integer(4),tital varchar(20),price float(5,2))"
#cur.execute(S)

#To insert table
#s="INSERT INTO book  (bookid,tital,price)  VALUES (%s, %s, %s)"

#to insert single input
#b1=(1, 'Python3',345)
#cur.execute(s,b1)        #  cur.execute()  it will make changes in database
#mydb.commit()            #  mydb.commit()  is used to save permenent chabges

#To insert multiple input
#books=[(2,'PHP',135),(3,'JAVA',40),(4,'HTML',200)]
#cur.executemany(s,books)
#mydb.commit()

#to fetch content of table
#s="SELECT * from book"
#cur.execute(s)
#result=cur.fetchall()
#for rec in result:
#    print(rec)

#to update table
#s="UPDATE book SET price=price+10 WHERE price>200"
#cur.execute(s)
#mydb.commit()  

#to delete total table
#s="DELETE form book"

#to delete perticular item
#s="DELETE from book WHERE tital='PHP' "
#cur.execute(s)
#mydb.commit