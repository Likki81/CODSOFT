a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
print("Menu")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
choice=int(input("Read a choice"))
if choice==1:
    print("Addition is",a+b)
elif choice==2:
    print("Substraction is",a-b)
elif choice==3:
    print("Multiplication is",a*b)
elif choice==4:
    print("Division is ",a/b)
else:
    print("Invalid choice")