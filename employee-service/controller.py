from mysql.connector import connect, Error
from employee import Employee
from datetime import datetime

class EmployeeController:
    def __init__(self, host, user, password, database):
        self.db_config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database
        }
    
    def get_connection(self):
        return connect(**self.db_config)
    
    def get_all_employees(self):
        try:
            with self.get_connection() as connection:
                with connection.cursor(dictionary=True) as cursor:
                    cursor.execute("SELECT fullname, birthdate, address, contact_number, emergency_number FROM employees")
                    results = cursor.fetchall()
                    return [Employee(**{k: v if k != 'birthdate' else datetime.strptime(str(v), '%Y-%m-%d') 
                                     for k, v in row.items()}) for row in results]
        except Error as e:
            print(f"Error: {e}")
            return []
    
    def get_employee_by_name(self, fullname):
        try:
            with self.get_connection() as connection:
                with connection.cursor(dictionary=True) as cursor:
                    cursor.execute("SELECT fullname, birthdate, address, contact_number, emergency_number FROM employees WHERE fullname = %s", (fullname,))
                    result = cursor.fetchone()
                    if result:
                        return Employee(**{k: v if k != 'birthdate' else datetime.strptime(str(v), '%Y-%m-%d') 
                                        for k, v in result.items()})
                    return None
        except Error as e:
            print(f"Error: {e}")
            return None
    
    def create_employee(self, employee_data):
        try:
            with self.get_connection() as connection:
                with connection.cursor() as cursor:
                    sql = """INSERT INTO employees 
                            (fullname, birthdate, address, contact_number, emergency_number) 
                            VALUES (%s, %s, %s, %s, %s)"""
                    cursor.execute(sql, (
                        employee_data['fullname'],
                        employee_data['birthdate'],
                        employee_data['address'],
                        employee_data['contact_number'],
                        employee_data['emergency_number']
                    ))
                    connection.commit()
                    return True
        except Error as e:
            print(f"Error: {e}")
            return False
