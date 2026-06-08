def adding():
    a=int(input("Enter a number: "))
    b=int(input("Enter a number: "))
    sum=a+b
    print("The Sum is :",sum)

def multiplication():
    a=int(input("Enter a number: "))
    b=int(input("Enter a number: "))
    mul=a*b
    print("The multiplication is :",mul)
    
def division():
    a=int(input("Enter a number: "))
    b=int(input("Enter a number: "))
    div=a/b
    print("The Division is :",div)

def subtraction():
    a=int(input("Enter a number: "))
    b=int(input("Enter a number: "))
    sub=a-b
    print("The Subtraction is :",sub)
    
print("Select user one input \n1.Addition \n2.Multiplication \n3.Division \n4.Subtraction")

user=int(input("Choose number: "))
if user==1:
    adding()
elif user==2:
    multiplication()
elif user==3:
    division()
elif user==4:
    subtraction()
else :
    print("error")
