#Import all the necessary Libraries
from employees import employee
import sqlite3
conn=sqlite3.connect("employees.db")
cursor=conn.cursor()
class employeeDao:
        
        def create_employee(employee):
            with conn:
                cursor.execute("INSERT INTO employee VALUES(:empcode,:firstname,:lastname,:age,:gender,:salary,:city,:state,:country)",
                {'empcode':employee.emp_code,'firstname':employee.first_name,'lastname':employee.last_name,'age':employee.age,'gender':employee.gender,
                'salary':employee.salary,'city':employee.city,'state':employee.state,'country':employee.country} )
        #This function retrieves employees from DB based on City
        def get_employee_by_city(city):
            cursor.execute("SELECT * FROM employee WHERE city=:city",{'city':city})
            return cursor.fetchall()
        #This function retrieves employees from DB based on employeeCode
        def get_employee_by_code(emp_code):
            cursor.execute("SELECT * FROM employee WHERE emp_code=:emp_code",{'emp_code':emp_code})
            return cursor.fetchall()
        #Updates city based on the firstname and lastname 
        def update_city(employee,city):
            with conn:
                cursor.execute("""UPDATE employee SET city=:city
                WHERE  emp_code=:empcode""",
                {'empcode':employee.emp_code,'city':city})
        #This function Deletes an employees record from the database
        def delete_employee(employee):
            with conn:
                cursor.execute("DELETE FROM employee WHERE emp_code=:empcode",
                {'empcode':employee.emp_code})
               # return cursor.delete()
        #This function returns all the employees in the DB
        def view_employees():
            with conn:
                cursor.execute("SELECT * FROM employee")
                return cursor.fetchall()
        #Create objects of the employee class and call the create employee function
        #employee_1 = employee('empl001','Nelson','Attah',35,'Male',2000.00,'Port-Harcourt','Rivers','Nigeria')
        #employee_2 = employee('empl002','Catherine','Attah',28,'Male',2000.00,'Port-Harcourt','Rivers','Nigeria')
        #create_employee(employee_1)
        #create_employee(employee_2)
        #print(get_employees('Port-Harcourt'))
        #conn.close()
        
            





