import mysql.connector
conn = mysql.connector.connect(host='localhost', password='Kunals#2004', user='root', database='youtube')
if(conn.is_connected()):
    print("connected")