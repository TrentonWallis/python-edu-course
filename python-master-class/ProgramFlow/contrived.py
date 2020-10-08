numbers = [1, 45, 32, 12, 60]
for number in numbers:
    if number % 8 ==0:
        print("The nums are not acceptable")
        break
else:
    print("All those nums are fine.")
