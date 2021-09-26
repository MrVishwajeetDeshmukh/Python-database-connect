import mysql.connector

mydb=mysql.connector.connect(
    host='localhost', 
    user='root', 
    password='123456789',  #put your MySQL password
    database='db1')
print(mydb.connection_id)

cur=mydb.cursor()


'''To create database'''
S="CREATE TABLE book (bookid integer(4),title varchar(20),price float(5,2))"
cur.execute(S)

'''To insert table'''
s="INSERT INTO book  (bookid,title,price)  VALUES (%s, %s, %s)"

'''to insert single input'''
# bookid=int(input("Enter book id:-"))
# title=(input("Enter book title:-"))
# price=int(input("Enter book price:-"))
# b1=(bookid, title ,price)
# cur.execute(s,b1)        #  cur.execute()  it will make changes in database
# mydb.commit()            #  mydb.commit()  is used to save permenent chabges

'''To insert multiple input'''
n=int(input("Enter no. of input :-"))
book=[]
for i in range (n):
    bookid=int(input("Enter book id:-"))
    title=(input("Enter book title:-"))
    price=int(input("Enter book price:-"))
    book.append((bookid, title, price))


# book=[(2,'PHP',135),(3,'JAVA',40),(4,'HTML',200)]
cur.executemany(s,book)
mydb.commit()

'''to fetch content of table'''
#s="SELECT * from book"
#cur.execute(s)
#result=cur.fetchall()
#for rec in result:
#    print(rec)

'''to update table'''
#s="UPDATE book SET price=price+10 WHERE price>200"
#cur.execute(s)
#mydb.commit()  

'''to delete total table'''
#s="DELETE form book"

'''to delete perticular item'''
#s="DELETE from book WHERE title='PHP' "
#cur.execute(s)
#mydb.commit

'''To delete database'''
#s="DROP database db1"
