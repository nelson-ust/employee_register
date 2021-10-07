class employee():
    def __init__(self,emp_code,first,last,age,gender,salary,city,state,country):
        # Employee class initialization with a new employee details
        self.emp_code =emp_code
        #self.Emp_code=empcode
        self.first_name=first
        self.last_name=last
        self.age=age
        self.gender=gender
        self.salary=salary
        self.city=city
        self.state=state
        self.country=country
    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first_name,self.last_name)

    @property  
    def fullname(self):
        return '{} {}'.format(self.first_name,self.last_name)
    def __repr__(self):
        return "Employee('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
            self.id,
            self.last_name,
            self.first_name,
            self.age,
            self.gender,
            self.salary,
            self.city,
            self.state,
            self.country)
