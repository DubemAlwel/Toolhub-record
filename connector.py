import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="toolhub_db")

mycursor = mydb.cursor()

mycursor.execute("show databases")

