import mysql.connector
from mysql.connector import Error

def insert_employee():
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
    
    except Error as error:
        print(f"Insert data failed: {error}")
    
    finally:
        if con.is_connected():
            cur.close()
            con.close()
            print("MySQL Connection is now CLOSED.")

def delete_employee():
    emp_id = input("Enter employee ID to delete: ")
    
    try:
        con = mysql.connector.connect(host='localhost', database='employee', user='root', password='')
        cur = con.cursor()
        
        query = "DELETE FROM emp_info WHERE emp_id = %s"
        cur.execute(query, (emp_id,))
        
        if cur.rowcount > 0:
            con.commit()
            print("Employee deleted successfully!")
        else:
            print("No employee found with the given ID.")
    
    except Error as error:
        print(f"Delete operation failed: {error}")
    
    finally:
        if con.is_connected():
            cur.close()
            con.close()
            print("MySQL Connection is now CLOSED.")

def update_employee():
    emp_id = input("Enter employee ID to update: ")
    column = input("Enter column to update (emp_name, date_of_birth, address, contact_no, emergency_no): ")
    new_value = input("Enter new value: ")
    
    try:
        con = mysql.connector.connect(host='localhost', database='employee', user='root', password='')
        cur = con.cursor()
        
        query = f"UPDATE emp_info SET {column} = %s WHERE emp_id = %s"
        cur.execute(query, (new_value, emp_id))
        
        if cur.rowcount > 0:
            con.commit()
            print("Employee updated successfully!")
        else:
            print("No employee found with the given ID.")
    
    except Error as error:
        print(f"Update operation failed: {error}")
    
    finally:
        if con.is_connected():
            cur.close()
            con.close()
            print("MySQL Connection is now CLOSED.")

def search_employee():
    emp_id = input("Enter employee ID to search: ")
    
    try:
        con = mysql.connector.connect(host='localhost', database='employee', user='root', password='')
        cur = con.cursor()
        
        query = "SELECT * FROM emp_info WHERE emp_id = %s"
        cur.execute(query, (emp_id,))
        result = cur.fetchone()
        
        if result:
            print("Employee Details:")
            print(result)
        else:
            print("No employee found with the given ID.")
    
    except Error as error:
        print(f"Search operation failed: {error}")
    
    finally:
        if con.is_connected():
            cur.close()
            con.close()
            print("MySQL Connection is now CLOSED.")

# Example usage:
while True:
    print("\n1. Add Employee\n2. Delete Employee\n3. Update Employee\n4. Search Employee\n5. Exit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        insert_employee()
    elif choice == '2':
        delete_employee()
    elif choice == '3':
        update_employee()
    elif choice == '4':
        search_employee()
    elif choice == '5':
        break
    else:
        print("Invalid choice! Please enter 1, 2, 3, 4, or 5.")













