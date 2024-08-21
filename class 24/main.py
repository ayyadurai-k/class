# class Person: #CLASS
#     def __init__(self,name,m1,m2,m3): #CONSTRUCTOR
#         self.name = name
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
    
#     def find_total(self): #METHODs
#         print("Total Mark Is : ", self.m1 + self.m2 + self.m3)
    
#     def display_name(self): #METHODs
#         print("Name Is : ", self.name)
    

        

# p1 = Person("Yesvanth",5,10,15) # OBJECT
# p2 = Person("Karthik",3,5,7)


# p1.display_name()

# p2.display_name()
# p2.find_total()


# STATIC METHODS

class Maths(): 
      
    @staticmethod
    def addNum(num1, num2): 
        return num1 + num2 

ans = Maths.addNum(1, 2) 
print("The result is", ans)