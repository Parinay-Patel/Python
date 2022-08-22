import time
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)#sleep(2) consider 2 second as a second
        t -= 1
    print("Thanks for using my countdown watch")
    
print("Welcome to Parinay's Watch")
t = int(input("Enter the time in seconds: "))
countdown(t)
