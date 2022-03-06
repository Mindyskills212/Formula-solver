#Algebric program
print("Algebraic Avengers By FareedDevelopers")
start = int(input('Select the formula :- 1:(a+b)square, 2:(a-b)square, 3:(a+b-c)square, 4:(a-b+c)square, 5:a square - b square : '))
a = int(input("Enter the value of 'a' : "))
b = int(input("Enter the value of 'b' : "))
c = int(input("Enter the value of 'c' : "))
if start == 1:
    print("^^^ a**2 + 2(a)(b) + b**2 ^^^")
    print((a+b)**2)

elif start == 2:
    print("^^^ a**2 - 2(a)(b) + b**2 ^^^")
    print((a-b)**2)

elif start == 3:
    print((a+b-c)**2)

elif start == 4:
    print((a-b+c)**2)

elif start == 5:
    print("^^^ (a+b)(a-b)^^^")
    print((a**2-b**2))

else :
    print("ERROR !!!")