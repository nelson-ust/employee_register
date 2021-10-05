import sqlite3
conn=sqlite3.connect("employees.db")
cursor=conn.cursor()
        #Create the emloyee table
cursor.execute("""CREATE TABLE employee(
            emp_code text,
            last_name text,
            first_name text,
            age integer,
            gender text,
            salary DECIMAL(10,5),
            city text,
            state text,
            country text
        )""")
        #make changes to the database
conn.commit()
#close the database connection
#conn.close()