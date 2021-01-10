def fizz_buzz(n: int) -> str:
    """
    Fizz Buzz Game
    Pass in an int `n` if divisble by 3 it will return "fizz"
    and if it divisble by 5 it will return "buzz", if divisble
    by both it will return "fizz buzz", any other number will return
    the str of that number.
    """
    text_string = ""
    divisble = False
    if n % 3 == 0:
        text_string += "fizz"
        divisble = True
    if n % 5 == 0:
        if text_string == "":
            text_string += "buzz"
        else:
            text_string += " buzz"
        divisble = True
    if divisble == False:
        text_string = str(n)


    return text_string


max_num = 100
min_num = 1

for i in range(max_num + 1):
    print(fizz_buzz(i))