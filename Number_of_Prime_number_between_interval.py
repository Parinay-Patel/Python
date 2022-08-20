# Python Program to Print all Prime Numbers in an Interval

def prime(a,b):
  for i in range(a, b+1):
   # Print Prime Numbers are Greater than 1
     if i > 1:
         for j in range(2, i):
             if (i%j) == 0:
                break
         else:
             print(f"{i}\n")

x = int(input("Enter lower value :"))
y = int(input("Enter upper value :"))
print(f"Prime numbers between {x} and {y} are : ")
prime(x,y)
