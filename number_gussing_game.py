from levels import easy_level, medium_level, hard_level

print("Number Guessing Game".center(100))
print("Chose a number between 1 and 100".center(100))
game_level = input("Chose a difficulty level:"
                   " Easy press '0', Medium press '1' and Hard press '2': ".center(100))
if game_level == '0':
    easy_level()
elif game_level == '1':
    medium_level()
elif game_level == '2':
    hard_level()
else:
    print("Wrong Entry!!")
