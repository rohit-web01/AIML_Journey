num = int(input("Enter Your Number: "))

def factorial(num) :
    fact = 1
    for i in range(1, num+1) : 
        fact = fact * i
    return fact

print("Factorial of", num, "is :", factorial(num))