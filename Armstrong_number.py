# Python Program to Check Armstrong Number/Narcissistic number

n = int(input("Enter a number : "))
sum = 0
if n<0:
    print("Enter a Positive number.")
else:
    t=n
    while t > 0:
      a=t%10
      sum+=a**3
      t//=10
if n>=10:
    if n==sum:
       print("Armstrong.")
    else:
       print("Not Armstrong.")
else:
    print("Not Armstrong.")
