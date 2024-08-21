#INHERITANCE - REUSABILITY

class StudentProfile: # PARENT OR SUPER
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print("Name : ", self.name)
        print("Age : ", self.age)



class StudentMarks(StudentProfile): #CHILD OR SUB
    def __init__(self, name, age, marks):
        super().__init__(name, age) # CALL PARENT CLASS __INIT__ METHOD
        self.marks = marks

    def display_marks(self):
        print("Marks : ", self.marks)

obj = StudentMarks("Yesvnath" , 17 , "17,18,20")

obj.display_info()
obj.display_marks()