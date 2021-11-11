number=int(input("enter the number"))
if number>=80:
    print("A grade")
elif number>=60 and number<=80:
    print("B grade")
elif number>=50 and number<=60:
    print("C grade")
elif number>=45 and number<=50:
    print("D grade")
elif number>=25 and number<=45:
    print("E grade")
else:
    print("F grade")