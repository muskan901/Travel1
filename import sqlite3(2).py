import mysql.connector
import sqlite3

mydb = mysql.connector.connect(host="localhost",user="root",password="*muskan*")
conn = sqlite3.connect('booking.db')
a = conn.cursor()
# conn.execute("CREATE TABLE book (Username CHAR(25), phone INT(10), email VARCHAR(50), traveldate DATE,nights INT(10), travelers INT(10))")
# conn.execute("SHOW TABLES")

# for x in conn:
#   print(x)
a = conn.cursor()
a.execute("SELECT * FROM book")
myresult = a.fetchall()
for x in myresult:
  print(x)
