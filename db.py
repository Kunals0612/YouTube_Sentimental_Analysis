import mysql.connector
conn = mysql.connector.connect(host='localhost', password='', user='root', database='youtube')
if(conn.is_connected()):
    print("connected")
