def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def floatQuotient(x, y):
    return x / y
def reminder(x, y):
    return x % y
def integerQuotient(x, y):
    return x // y
def power(x, y):
    return x ** y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Quotient(Float)")
print("5.Reminder")
print("6.Quotient(Integer)")
print("7.Power(x^y)")

while True:
    choice = input("Enter choice(1/2/3/4/5/6/7): ")
    if choice in ('1', '2', '3', '4', '5', '6', '7'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {floatQuotient(num1, num2)}")
        elif choice == '5':
            print(f"{num1} / {num2} = {reminder(num1, num2)}")
        elif choice == '6':
            print(f"{num1} / {num2} = {integerQuotient(num1, num2)}")
        elif choice == '7':
            print(f"{num1} ^ {num2} = {power(num1, num2)}")
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")
