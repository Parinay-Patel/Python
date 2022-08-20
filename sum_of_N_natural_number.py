# Python Program to Find the Sum of Natural Numbers

n = int(input("Enter the number of terms : "))

sum=0
for i in range(0,n+1):
    sum=sum+i
print(f"Sum of first {n} Natural number = {sum}")
