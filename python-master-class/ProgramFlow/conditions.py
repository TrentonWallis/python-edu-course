age = int(input("How old are you?"))
if age in range(16, 66): # in and it will find the first condition that is false
    print("Have a good day at work")
else:
    print("Enjoy your free time")

print("-" * 80)

if age < 16 or age > 65: # in or it will find the first condition that is true
    print("Enjoy your free time")
else:
    print("Have a good day at work")
