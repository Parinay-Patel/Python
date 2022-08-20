# Python Program to Check Whether a String is Palindrome or Not

a = str(input("Enter a string : "))
a = a.casefold()
b = reversed(a)
if list(a) == list(b):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")
