month=input("enter the month:")
if month=="feb":
    print("No.of days:28/29")
elif month in ("jan","march","may","july","sep","nov"):
    print("No.of days:30")
elif month in ("april","june","aug","oct","dec"):
    print("No.of days:31")
else:
    print("no days")