import random
highest = 10
answer = random.randint(1, 10)
print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input())


while guess is not answer:

    if guess == 0:
        print("You have exited the game.")
        break

    if guess < answer:
        print("Please guess higher")
        guess = int(input())
    elif guess > answer:
        print("Please guess lower")
        guess = int(input())

else: # will only print if get through game all the way
    print("Well done you guessed correctly")






# if guess < answer:
#     print("Please guess higher.")
#     guess = int(input())
#     if guess == answer:
#         print("Well done you guessed it")
#     else:
#         print("Sorry you did not guess correctly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done you guessed it")
#     else:
#         print("Sorry you did not guess correctly")
# else:
#     print("You win! You got it the first time!")
#
#
