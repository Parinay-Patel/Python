import random
import string

def password(length):
    letters = string.ascii_lowercase
    result_str = "".join(random.choice(letters) for i in range(length))
    print(f"Random string of length {length} is: {result_str}")

a = int(input("Enter the length of password : "))
password(a)
