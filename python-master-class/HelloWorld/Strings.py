print("Today is a good day to learn Python")
print ('Python is fun')
print("Python's string are easy to use")
print('We can even include "quotes" in strings')
print("hello" + " world")

greeting = "Hello"
name = "Trenton"
print(greeting + name)
# if we want space we just add it
print(greeting + " " + name)

age = 20

print(type(greeting))
print(type(age))
print(name + f" is {age} years old")  # cannot concat int and strings
age = "2 years"  # rebind
age_in_words = "20 years"


print(name + " is " + age + " old")

print(f"Pi is approximately {22 / 7:12.50f}")
pi = 22/7
print(f"Pi is approzimately {pi:12.50f}")
