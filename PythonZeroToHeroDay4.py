#Defining a function which will take a number as argument and return its factorial
def facto (f):
    fact=1
    for p in range (f,0,-1):
        fact=fact*p
    return fact
number=int(input("Enter a number ",))
result=facto(number)
print("Factorial of",number,"is",result)