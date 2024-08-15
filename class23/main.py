age=18
name = "Yesvanth"

ages = [18,19,17,16,20]
names = ["Yesvanth", "Karthik","Kumar","Bala","Vinoth"]

# CLASS 

class Person: #CLASS
    def __init__(self, name, age): # INITIALIZATION
        self.name = name
        self.age = age

n = int(input("How Many Peoples : "))

persons = []

for i in range(n): #2
    name = input("Enter Name : ")
    age = int(input("Enter Age : "))
    obj = Person(name, age) #OBJECT CREATION 
    persons.append(obj) # APPEND OBJECT TO LIST

# persons = [obj,obj]



for person in persons:
    print(person.name, person.age)


