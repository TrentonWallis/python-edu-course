# parrot = "Norwegian Blue"
# print(parrot)
# print(parrot[-11])
# print(parrot[-10])
# print(parrot[-5])
# print(parrot[-11])
# print(parrot[-8])
# print(parrot[-6])
#
# print(parrot[0:6])
# print(parrot[-14:-8])
#
#
# print(parrot[-4:-2])  # cannot do pos 2 counts right to left
# print(parrot[-4:12])
#
#
# # steps
# #Nre
# print(parrot[0:6:2])  # up to but not including 6 insteps of 2
# #Nw
# print(parrot[0:6:3]) # up to but not including 6 insteps of 3

number = input("Please enter numbers that are separated: ")
separators = ""
for char in number:
    if not char.isnumeric():
        separators = separators + char
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))



