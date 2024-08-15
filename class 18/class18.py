# try :
#     list1 = [1,2,3,4,5,6,7,8,9,10]
#     print(list1[5]) #RAISE ERROR
#     print(list1[3])
#     raise Exception("Manual Error Raising ")
#     # result = 'hello' + 5
# except IndexError:
#     print("Index Out of Range")
# except NameError:
#     print("Check variable name")
# except Exception:
#     print("Unknown Error")
# finally:
#     print("Program Finished")


age = 17

try :
    if age < 18 :
        raise ValueError("Age should be 18 or above")
    print("Welcome")
except ValueError:
    print("Invalid Age")
