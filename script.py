age = int(input("Enter age: "))
if(age<1):
    print("Infant")
elif(age<13 and age>1):
    print("child")
elif(age>13 and age<19):
    print("Teenager")
else:
    print("Adult")
