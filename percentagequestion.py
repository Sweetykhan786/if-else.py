phy = float(input("enter the marks:"))
chemis = float(input("enter the marks:"))
bio = float(input("enter the marks:"))
mathe = float(input("enter the marks:"))
comp = float(input("enter the marks:"))
total = phy+chemis+bio+mathe+comp
percentage = (total/500)*100
if percentage>=90:
    print("Grade A")
elif percentage>=80:
    print("Grade B")
elif percentage>=70:
    print("Grade C")
elif percentage>=60:
    print("Grade D")
elif percentage>=40:
    print("Grade E")
else:
    print("Grade F")
