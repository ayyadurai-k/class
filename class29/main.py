
# POLYMORPHISM

# 1. METHOD OVERRIDING

# class Parent:
#     a = 10
#     def print_some(self):
#         print("From parent class")

# class Child(Parent):
#     a = 15
#     def print_some(self):
#         print("From child class")

# obj = Child()

# print(obj.a)
# obj.print_some()

#2 . OVERLOADING - NOT SUPPORTED BY PYTHON 

class Parent:
    def add(self, x, y):
        print("Called from parent class")
        return x + y

class Child(Parent):
    def add(self, x, y, z):
        print("Called from child class")
        return x + y + z

obj = Child()

print(obj.add(10, 20,30))