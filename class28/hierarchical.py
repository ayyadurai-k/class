class Parent:
    def print_parent(self):
        print("From parent")

class Child1(Parent):
    def print_child1(self):
        print("From child1")

class Child2(Parent):
    def print_child2(self):
        print("From child2")

c1 = Child1()
c1.print_parent()
c1.print_child1()

c1.print_child2()