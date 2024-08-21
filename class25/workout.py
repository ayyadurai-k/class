class Student:
    def __init__(self, name, age, m1,m2,m3):
        self.name = name
        self.age = age
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    
    def get_grade(self):
        self.avg = (self.m1 + self.m2 + self.m3) / 3 # PRIORITIZE THE OPERATION

        if self.avg >= 90:
            return "A"
        elif self.avg >= 80:
            return "B"
        elif self.avg >= 70:
            return "C"
        elif self.avg >= 60:
            return "D"
        else:
            return "F"
    
    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.m1, self.m2, self.m3)
        print("Grade:", self.get_grade())
        print("Average:", self.avg)



n = int(input("How many students :"))

students = []

# GET INPUT AND CRETE OBJECTS
for i in range(n):
    name = input("Enter Name : ")
    age = int(input("Enter Age : "))
    m1 = int(input("Enter Mark 1 : "))
    m2 = int(input("Enter Mark 2 : "))
    m3 = int(input("Enter Mark 3 : "))
    
    obj = Student(name, age, m1, m2, m3)
    students.append(obj)

# DISPLAY DETAILS OF ALL STUDENTS
for student in students:
    student.display_details()