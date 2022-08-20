# Python Program to Find the Factorial of a Number

def factorial(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    print(f"Factorial of {n} = {product}")

a = int(input("Enter a number : "))
a = factorial(a)
