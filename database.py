import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="nana",
    database="document_management"
)

cursor = connection.cursor()