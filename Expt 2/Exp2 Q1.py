age=int(input("Enter Your age:"))
if age<=12:
    print("Child")
elif age>=13 and age<=19:
    print("Teen")
elif age>=20 and age<=65:
    print("Adult")
else:
    print("Senior Citizen")
