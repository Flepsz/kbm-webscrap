import mysql.connector


con = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='kabum'
)

cursor = con.cursor()
