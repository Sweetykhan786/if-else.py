triangle1 = int(input("enter the first angle of triangle:"))
triangle2 = int(input("enter the second angle of triangle:"))
triangle3 = int(input("enter the third angle of triangle:"))
total= triangle1+triangle2+triangle3
if total == 180:
    print("valid triangle")
else:
    print("not valid")