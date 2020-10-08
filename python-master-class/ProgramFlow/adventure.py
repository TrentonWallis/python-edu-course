exits = ["north", "south", "east", "west"]
chosen_exit = ""
while chosen_exit not in exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit == "quit":
        print("Game over")
        break
else:
    print("arent you glad you got out of there?")

