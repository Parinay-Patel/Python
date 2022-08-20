# Python Program to Find LCM

def lcm(x, y):
   if x > y:
       great = x
   else:
       great = y
   while(True):
       if((great % x == 0) and (great % y == 0)):
           lcm = great
           break
       great+=1
   return lcm

a = int(input("Enter number1 : "))
b = int(input("Enter number2 : "))
print(f"The L.C.M. is {lcm(a,b)}")
