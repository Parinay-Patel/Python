# Python Program to Find the Factors of a Number

from re import I


n = int(input("Enter a number : "))
if n==0:
    print("Only 1 factor i.e. 0")
else:
    for i in range(1,n):
        if n%i==0:
            print(f"{i} X", end=" ")
        else:
            pass
