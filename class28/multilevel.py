class GrandFather:
    def print_grand_father(self):
        print("From Grand Father")

class Father(GrandFather):
    def print_father(self):
        print("From Father")

class Child(Father):
    def print_child(self):
        print("From Child")

obj = Father()

obj.print_grand_father()

obj.print_father()


