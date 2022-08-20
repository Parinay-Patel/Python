# Python Program to Find HCF or GCD

def hcf(x, y):
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small+1):
        if((x % i == 0) and (y % i == 0)):
            h=i 
    return h

a = int(input("Enter number1 :"))
b = int(input("Enter number2 :"))
print(f"The H.C.F. is {hcf(a,b)}")
