shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"
                 ]

another_list = shopping_list

print(id(shopping_list))
print(id(another_list)) # Will be the same as above

shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))
print(id(another_list))
print(another_list)

a = b = c = d = e = f = another_list # One list with 8 names

print("Adding cream")
b.append("cream")
print(c)
print(d)
