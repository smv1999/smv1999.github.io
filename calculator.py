c='y'
print("CALCULATOR")
while c=='y':
    print("1.Addition 2.Subtraction 3.Multiplication 4.Division")
    ch=int(input("Enter your choice:"))
    if(ch==1):
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        print("Addition of the two numbers:",a+b)
    elif(ch==2):
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        print("Subtraction of the two numbers:",a-b)
    elif(ch==3):
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        print("Multiplication of the two numbers:",a*b)
    elif(ch==4):
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        try:
            print("Division of the two numbers:",a/b)
        except:
            print("Division by zero Error!")
    else:
        print("Invalid choice!")
    c=input("Do you wanna continue?(y/n)")    