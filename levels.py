import random

number = random.randint(1, 100)
print(number)


def easy_level():
    """
    easy level of number guessing game
    :return: do not return anything
    """
    counter = 10
    attempts = 1
    print("You have 10 attempts".center(100))
    while counter > 0:
        guess = int(input("Number: "))
        if guess > 100 or guess < 0:
            print("Do not type a number greater then 100 and less then 0")
        if guess > number:
            counter -= 1
            attempts += 1
            print("Too high!")
            if counter == 0:
                pass
            else:
                print(f"You have {counter} attempts")
                print("")
        elif guess < number:
            counter -= 1
            attempts += 1
            print("Too low!")
            if counter == 0:
                pass
            else:
                print(f"You have {counter} attempts")
                print("")
        else:
            print(f"You got the answer in {attempts} attempts\nAnswer is {number}")
            break
        if counter == 0 and guess != number:
            print("You Lose!")
            break


def medium_level():
    """
    medium level of number guessing game
    :return: do not return anything
    """
    counter = 7
    attempts = 1
    print("You have 7 attempts".center(100))
    while counter > 0:
        guess = int(input("Number: "))
        if guess > 100 or guess < 0:
            print("Do not type a number greater then 100 and less then 0")
        if guess > number:
            counter -= 1
            attempts += 1
            print("Too high!")
            if counter == 0:
                pass
            else:
                print(f"You have {counter} attempts")
                print("")
        elif guess < number:
            counter -= 1
            attempts += 1
            print("Too low!")
            if counter == 0:
                pass
            else:
                print(f"You have {counter} attempts")
                print("")
        else:
            print(f"You got the answer in {attempts} attempts\nAnswer is {number}")
            break
        if counter == 0 and guess != number:
            print("You Lose!")
            break


def hard_level():
    """
    hard level of number guessing game
    :return: do not return anything
    """
    counter = 4
    attempts = 1
    print("You have 4 attempts".center(100))
    while counter > 0:
        guess = int(input("Number: "))
        if guess > 100 or guess < 0:
            print("Do not type a number greater then 100 and less then 0")
        if guess > number:
            counter -= 1
            attempts += 1
            print("Too high!")
            if counter == 0:
                pass
            else:
                print(f"You have {counter} attempts")
                print("")
        elif guess < number:
            counter -= 1
            attempts += 1
            print("Too low!")
            if counter == 0:
                pass
            else:
                print(f"You have {counter} attempts")
                print("")
        else:
            print(f"You got the answer in {attempts} attempts\nAnswer is {number}")
            break
        if counter == 0 and guess != number:
            print("You Lose!")
            break
