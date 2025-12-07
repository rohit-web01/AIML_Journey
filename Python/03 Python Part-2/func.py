name = input("Enter your name : ")
a = int(input("Enter a : "))
b = int(input("Enter b : "))

def sum (a,b):  # parameters
    s = a+b
    return s


def greet(name) :
    print("Hello,",name,"Wassup!")
    print("Sum of",a,"and",b,"is : ",sum(a,b))


greet(name) #arguments