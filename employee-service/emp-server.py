from flask import Flask
from routes import employee_bp
from dotenv import load_dotenv
import os
import mysql.connector
from mysql.connector import Error

# Load environment variables
load_dotenv()

def init_database():
    # First connection to create database if it doesn't exist
    try:
        conn = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )
        
        if conn.is_connected():
            cursor = conn.cursor()
            
            # Read schema.sql file
            with open('schema.sql', 'r') as sql_file:
                # Split the content into individual commands
                sql_commands = sql_file.read().split(';')
                
                for command in sql_commands:
                    # Skip empty commands
                    if command.strip():
                        try:
                            cursor.execute(command)
                            conn.commit()
                        except Error as e:
                            print(f"Error executing SQL command: {e}")
                            
            print("Database initialized successfully!")
            
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

app = Flask(__name__)
app.register_blueprint(employee_bp, url_prefix='/employee')

if __name__ == '__main__':
    port = int(os.getenv('FLASK_PORT', 3001))
    
    # Initialize database before starting the server
    print("Initializing database...")
    init_database()
    
    print("╔════════════════════════════════════════╗")
    print("║         Employee Service API           ║")
    print("╠════════════════════════════════════════╣")
    print(f"║ Server running on port: {port}          ║")
    print("║ API endpoints:                         ║")
    print("║ • GET    /employee/all                ║")
    print("║ • POST   /employee/create             ║")
    print("╚════════════════════════════════════════╝")
    app.run(debug=True, port=port)
