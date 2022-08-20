# Python Program to Print the Fibonacci sequence

n = int(input("Enter, how many terms you want?"))

n1, n2 = 0, 1 #respectively
sum = 0

if n <= 0:
   print("Please enter a positive integer!")
elif n == 1:
   print(f"Fibonacci sequence upto {n} \n {n1}")
else:
   print("Fibonacci sequence:")
   for i in range(0,n):
      print(sum, end=" ")
      n1 = n2 #store the value of n2 in n2
      n2 = sum # store the value of sum in n1
      sum = n1 + n2 # add bot n1 and n2
