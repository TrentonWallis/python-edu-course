low = 1
high = 1000

print("Please thinkn of a number between {} and {}".format(low, high))
input("Press ENTER to start")

guesses = 1

while low != high:
    print("\tGuessing in the range of {} and {}".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or "
                     "lower? Enter h or l, or c if my guess was "
                     "correct".format(guess)).casefold()
    if high_low == "h":
        # Guess higher. The low end of the range becomes 1 greater than the guess
        low = guess + 1
    elif high_low == "l":
        high = guess - 1
        pass
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
    else:
        print("Please enter h, l, or c")

    # guesses = guesses +1 slower and less optimal
    guesses += 1