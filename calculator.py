#A simple calculator in python using dynamic inputs
print("welcome to the calculator")
print("")
while 1:
    a=int(input("first number"))
    b=int(input("second number"))
    print("1.Addition\t2.subtraction\t3.multiplication\t4.division")
    c=int(input("enter the number to perform calculation"))
    if c==1:
        print("result:",a+b)
    elif c==2:
        print("result:",a-b)
    elif c==3:
        print("result:",a*b)
    elif c==4:
        print("result:",a/b)
    else:
        print("invalid number")
