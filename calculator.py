def calculator():
    try:
        a=float(input("Enter the first number: "))
        b=float(input("Enter the second number: "))
        c=input("Choose the operation (+,-,*,/):")

        if c=="+":
            print(a+b)
        elif c=="-":
            print(a-b)
        elif c=="*":
            print(a*b)
        elif c=="/":
            print(a/b)
        elif c=="/" and (a==0 or b==0):
            print("can not divide by zero")
        else:
            print("Provide valid inputs")
    except ZeroDivisionError as e:  
        print(f"error-{e}")
    except ValueError:
        print('Print only value numbers')
calculator()