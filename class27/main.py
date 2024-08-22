class Employee:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department
    
    def display_info(self):
        print("Name : ", self.name)
        print("Age : ", self.age)
        print("Department : ", self.department)

class Salary(Employee):
    def __init__(self, name, age, department, salary): 
        super().__init__(name, age, department)
        self.salary = salary
    
    def display_salary(self): 
        print("Salary : ", self.salary)
    

e1 = Salary("John Doe", 30, "IT", 50000)

e1.display_info()
e1.display_salary()