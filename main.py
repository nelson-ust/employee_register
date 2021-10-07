from employees import employee
from employee_dao import employeeDao
import sqlite3
import sys
#inherits the employee class from employees.py file
conn=sqlite3.connect("employees.db")
cursor=conn.cursor()
dao=employeeDao
#This method Accepts employees details as parameters and inserts the record into the db
def add_employee():
        #Accepts users inputs
     empcode=input("\nEnter Employee Code: ")
     first_name=input("\nEnter Firstname: ")
     last_name=input("Enter Lastname: ")
     age=input("\nEnter Age: ")
     gender= input("\nEnter Gender: ")
     salary= input("\nEnter Salary: ")
     city= input("\nEnter City: ")
     state= input("\nEnter State: ")
     country= input("\nEnter Country: ")
     #create and instance of the employee class
     newEmployee = employee
     newEmployee.emp_code = empcode
     newEmployee.first_name = first_name
     newEmployee.last_name = last_name
     newEmployee.age = age
     newEmployee.gender = gender
     newEmployee.salary = salary
     newEmployee.city = city
     newEmployee.state = state
     newEmployee.country = country
     dao.create_employee(newEmployee)
     print(f'The employee with firstname: {newEmployee.first_name }, Lastname: {newEmployee.last_name} and  Employee Code: {newEmployee.emp_code} has been Added Successfully!!!\n')

def transfer_employee():
   # first = input('Enter Firstname of the Employee you would like to Update: ')
    code = input('Enter EmployeeCode of the Employee you would like to Transfer: ')
    modify_employee = employee
    city = input(f"Enter city you want the employee with ID: {code} transfered to:  ")
    modify_employee.city = city
    dao.update_city(modify_employee,city) #modify_employee.city)
    print(f'\nThe Employee With ID: {code} has been successfully tranfered to {modify_employee.city} .')
def view_employee_by_city():
    #create an object of the employee class to map the city 
    emp_by_city = employee
    print('')
    print('To search Employees by City you will Have to specify the city')
    #Prompt the user for the new city and and map it to the city property of the employee object
    city =input('Enter City: ')
    emp_by_city.city = city
    emp_list=dao.get_employee_by_city(emp_by_city.city)
    print('------------------------------------------')
    print(emp_list)
#print
def view_employee_by_empCode():
    #create an object of the employee class and map the employeecode to the 
    emp_by_id = employee
    print('To search Employees by EmployeeCode you will Have to specify the Id of the Employee')
    emp_code =input('Enter EmployeeCode: ')
    emp_by_id.emp_code = emp_code
    emp = dao.get_employee_by_code(emp_code)
    print('--------------------------------------')
    print(emp)

    
def delete_employee():
    #
    print("To delete an employee Provide the following Informations\n")
    code = input("Enter Employee Code: ")
    #first = input('Enter Firstname of the Employee you like to remove: ')
    #last = input('Enter Lastname of the Employee you like to remove: ')
    del_employee = employee
    #del_employee.first_name = first
    #del_employee.last_name = last
    del_employee.emp_code = code
    dao.delete_employee(del_employee)
    print(f'The employee with EmployeeCode: {del_employee.emp_code} has been deleted successfully!!!')
def view_employees():
    staff=dao.view_employees()
    print(staff)
def main_menu():
    while True:
        print()
        print('''Please select one of the following:

            1.   Add Employee
            2.   View Employee by City
            3.   View Employee by EmployeeCode
            4.   View All Employees/Staff
            5.   Update an Employee - Transfer an employee
            6.   Delete an Employee
            7.   Quit
            ''')
        # Calls function based on corresponding number that the user inputs
        selection = input('Please enter an action: ')
        if selection == '1':
            # call the add_employee function
            add_employee()
            
        
        elif selection == '2':
            # Call the View_employee_by_city function
            view_employee_by_city()
        elif selection == '3':
            # Call the view_employee_by_empCode function
            view_employee_by_empCode()
        elif selection == '4':
            # Call the view_employees function
            view_employees()
        elif selection == '5':
            # Call the update_empployee function/method to modify the city of the employee
            transfer_employee()
        elif selection == '6':
            # Call the delete the employee with the specified first and last names.
            delete_employee()
        elif selection == '7':
            print('Thank you for using this Application!!!')
            sys.exit()

        else:
            print('Sorry You have enetered an Invalid Option')
            
main_menu()



 




