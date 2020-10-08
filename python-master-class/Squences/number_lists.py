empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]


numbers = even + odd
print(numbers)
sorted_numbers = sorted(numbers)    # sorted fucntion creates a new list, dangerous
                                    # when your list is very long.
print(sorted_numbers)
print(numbers)
digits = list("432985617")    # converts the string to a list
print(digits)

more_numbers = list(numbers)
print(more_numbers)
print(numbers is more_numbers)  # false: proof that it makes a different
print(numbers == more_numbers)  # true: shows they have the same items

sliced_numbers = numbers[:]
print(sliced_numbers)
copy_list = numbers.copy()
print(copy_list)
