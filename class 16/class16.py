# def hello(name="Unknown"): #DEFAULT ARGUMENT
#     print("Hello", name)

# hello("Yesvanth")


   
# def nameAge(name, age,b,area,state):
#     print("Hi, I am", name)
#     print("My age is ", age)
 
# # nameAge("Prince", 20) #POSITIONAL ARGUMENT => *
# nameAge(age=20,name="Prince") #KEYWORD ARGUMENT => **
 
# nameAge(age=20, name="Prince")

# def myFun(*argv):
#     print(argv)

# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

def myFun(**kwargs):
    print(kwargs)

  
# Driver code
myFun(first='Geeks', mid='for', last='Geeks')