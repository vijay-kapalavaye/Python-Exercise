percentage=int(input("enter your percentage :"))
if percentage>75 and percentage<100:
    print("O GRADE")
elif percentage<=75 and percentage>50:
    print("A GRADE")
elif percentage<=50 and percentage>25:
    print("B GRADE")
else:
    print('C GRADE')