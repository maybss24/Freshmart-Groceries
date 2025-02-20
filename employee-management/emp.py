import mysql.connector
from mysql.connector import Error

id = input("Enter employee id: ")  
name = input("Enter full name: ")
birth = input("Enter date of birth (YYYY-MM-DD): ")
add = input("Enter address: ")
contact = input("Enter contact no: ")
emergency = input("Enter emergency contact no: ")

try:
    con = mysql.connector.connect(host='localhost', database='employee', user='root', password='')
    cur = con.cursor()

    query = "INSERT INTO emp_info (emp_name, date_of_birth, address, contact_no, emergency_no) VALUES (%s, %s, %s, %s, %s)"
    cur.execute(query, (name, birth, add, contact, emergency))

    con.commit()
    print("Data inserted successfully!")

    cur.close()
except Error as error:
    print(f"Insert data failed: {error}")
finally:
    if con.is_connected():
        con.close()
        print("MySQL Connection is now CLOSED.")













