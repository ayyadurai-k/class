# multiple inheritance
 
class Mother:
    def print_mother(self):
        print("From Mother")
 
class Father: 
    def print_father(self):
        print("From Father")
    
    
 

class Son(Mother, Father):
    def print_son(self):
        print("From Son")


s = Son()
s.print_father()
s.print_mother()
s.print_son()