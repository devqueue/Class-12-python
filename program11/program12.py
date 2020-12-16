'''
Integrate SQL with Python by importing the MySQL module
'''
import os


import mysql.connector as sqltor
from mysql.connector import Error

connection = sqltor.connect(
    host='localhost', database='Haziq', user='root', password='c9070baa')

try:
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        cursor.execute("create table orders(ord_no int(6) not null, purch_atm float(6), ord_date date, customer_id int(4), salesman_id int(4);")
        cursor.execute('insert into orders values(70001,150.5,"2012-10-05",3005,5002')
        cursor.execute('insert into orders values(70009,270.65,"2012-09-10",3001,5005')
        cursor.execute('insert into orders values(70002,62.26,"2012-10-05",3002,5001')
        cursor.execute('insert into orders values(70004,110.5,"2012-08-17",3009,5003')
        connection.commit()

mycursor.execute("create table ORDERS(ord_no int(5) primary key, purch_amt decimal(8,2),ord_date date, customer_id int(4), salesman_id int (4))")
except Error as e:
    print(e)

finally:
    if (connection.is_connected()):
        cursor.execute('Show tables')
        record = cursor.fetchall()
        print(record)
        cursor.close()
        connection.close()
        print("MySQL connection is closed")