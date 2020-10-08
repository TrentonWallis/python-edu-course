
number = 100

while True:
    print("Select a food to learn more about it:\n"
          "1: Tea\n"
          "2: Pizza\n"
          "3: Cheese\n"
          "4: Milk\n"
          "0: Quit")
    number = int(input("Select an item: "))

    if number == 1:
        print("Tea: Leaves soaked in water!")
        continue
    elif number == 2:
        print("Pizza: Bread, Tomatoes, and Cheese!")
        continue
    elif number == 3:
        print("Cheese: Milk that is curdled!")
        continue
    elif number == 4:
        print("Milk: Cow juice!")
        continue
    elif number == 0: # better code if 0 is at top so it doesnt have check all to quit
        print("You have exited.")
        break







