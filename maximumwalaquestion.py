num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))
num3 = int(input("enter the third number:"))
if num1>=num2 and num1>=num3:
    print("num1, is maximum")
elif num2>=num1 and num2>=num3:
    print("num2, is maximum")
else:
    print("there is no maximum numbers")
