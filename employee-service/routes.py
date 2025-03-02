from flask import Blueprint, jsonify, request
from controller import EmployeeController
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

employee_bp = Blueprint('employee_bp', __name__)
employee_controller = EmployeeController(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_NAME')
)

@employee_bp.route('/all', methods=['GET'])
def get_employees():
    employees = employee_controller.get_all_employees()
    return jsonify([emp.to_dict() for emp in employees])

@employee_bp.route('/create', methods=['POST'])
def create_employee():
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['fullname', 'birthdate', 'address', 'contact_number', 'emergency_number']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        # Print received data for debugging
        print("Received data:", data)
        
        try:
            # Convert string date to datetime object
            birthdate = datetime.strptime(data['birthdate'], '%Y-%m-%d')
            data['birthdate'] = birthdate.date()
        except ValueError as e:
            return jsonify({'error': f'Invalid date format. Use YYYY-MM-DD format. Error: {str(e)}'}), 400
        
        success = employee_controller.create_employee(data)
        if success:
            return jsonify({
                'success': True,
                'message': 'Employee created successfully',
                'data': {
                    'fullname': data['fullname'],
                    'birthdate': data['birthdate'].strftime('%Y-%m-%d'),
                    'address': data['address'],
                    'contact_number': data['contact_number'],
                    'emergency_number': data['emergency_number']
                }
            }), 201
        return jsonify({'success': False, 'error': 'Failed to create employee'}), 400
        
    except Exception as e:
        print(f"Error creating employee: {str(e)}")
        return jsonify({'success': False, 'error': f'Server error: {str(e)}'}), 500
