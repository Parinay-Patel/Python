import random
a = int(input("How many dice you want to roll : "))
for i in range(1,a+1):
    diceValue = random.randint(1,6)
    print(f"Value of Dice{i}= {diceValue}")
print("Thank you for using our Dice :) ")
