print("this is a calculator")

x=int(input("enter any number"))
y=int(input("enter any number again"))
z=["add","subtract","multiply","divide"]
print(z)

s=str(input("enter an operation from the above"))


if s=="add":
    k=x+y
    print("after addition:",k)

elif(s=="subtract"):
    k=x-y
    print("after subtraction:",k)

elif(s=="multiply"):
    k=x*y
    print("after multiplication",k)

elif(s=="divide"):
    k=x/y
    print("after division:",k)

else:
    print("no result")
