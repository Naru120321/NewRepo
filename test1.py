import mysql.connector as con
mydb=con.connect(host="localhost",user="root",passwd="Naru@2108")
print(mydb)
cursor=mydb.cursor()
#cursor.execute("show databases")
print(cursor.execute("show databases"))

