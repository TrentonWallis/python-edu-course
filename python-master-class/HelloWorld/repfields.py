age = 24
print(("My age is {0} years").format(age))
# can use replacement field in a dot format method

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, and {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))

print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}"
      .format(28, 30, 31))