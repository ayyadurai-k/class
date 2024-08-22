# TYPE OF INHERITANCE

# 1. Single Inheritance : One class inherits from one parent class.
# 2. Multiple Inheritance : Multiple classes inherits from
# 3. Multilevel Inheritance : Multiple classes inherits from
# 4. Hierarchical Inheritance : Multiple classes inherits from
# 5. Hybrid Inheritance : More than one type

# 1. Single Inheritance : One class inherits from

class Parent:
    def from_parent(self):
        print("From Parent Class")

class Child(Parent):
    def from_child(self):
        print("From Child Class")

obj = Child()
obj.from_parent()
obj.from_child()