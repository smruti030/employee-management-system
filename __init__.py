from flask import Blueprint, jsonify, request
from models import db, Employee
from schemas import employee_schema, employees_schema

main = Blueprint('main', __name__)


# Route for the homepage
@main.route('/employees', methods=['GET'])
def home():
    return "Welcome to the Employee Management System", 200


# Get all employees
@main.route('/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    return employees_schema.jsonify(employees)

# Add a new employee
@main.route('/employees', methods=['POST'])
def add_employee():
    data = request.get_json()
   
    name=data['name']
    position=data['position']
    department=data['department']
    
    new_employee = Employee(name=name, position=position, department=department)

    db.session.add(new_employee)
    db.session.commit()
    return employee_schema.jsonify(new_employee), 201

# Update an employee
@main.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    employee = Employee.query.get_or_404(id)
    data = request.get_json()
    employee.name = data['name']
    employee.position = data['position']
    employee.department = data['department']
    db.session.commit()
    return employee_schema.jsonify(employee)

# Delete an employee
@main.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
    return '', 204
