for i in range(1, 13):
    print("No. {0:<2} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))
# {0:2} give you value pos 0 with a width of 2
# < can be used to left align
#^ can be used to centered

print()

print("pi is approximately {0:12}".format(22/7))
print("pi is approximately {0:12f}".format(22/7))
print("pi is approximately {0:12.50f}".format(22/7))
print("pi is approximately {0:52.50f}".format(22/7))
print("pi is approximately {0:62.50f}".format(22/7))
print("pi is approximately {0:<72.50f}".format(22/7))
print("pi is approximately {0:<72.54f}".format(22/7))

