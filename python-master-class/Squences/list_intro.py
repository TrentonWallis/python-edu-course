


computer_parts = ["computer", "monitor", "keyabord",
                  "mouse", "mouse mat"]

print(computer_parts)

# computer_parts[3] = "trackball"
print(computer_parts[3:])
# print(computer_parts)
computer_parts[3:] = ["trackball"] # if just a string then it is an iterable so that it wont insert as one word but
# the letters
print(computer_parts)