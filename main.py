from random_api import gen_random_ints
from usr_input_api import get_user_guess
from win_check_api import check_win, check_cows, check_bulls

game_rules = """
### RULES of the GAME ###

For every digit that you have guessed correctly in the correct place, you have a “cow”.

For every digit that you have  guessed correctly in the wrong place is a “bull.”

Every time you make a guess, we will print how many “cows” and “bulls” you have.

Once the you guess the correct number, the game is over.

Try to quess number in less than 20 attempts.
"""


def main():
    print(game_rules)
    number_to_guess = gen_random_ints()
    attempt_count = 1
    max_attempt_count = 20
    while attempt_count < max_attempt_count:
        curr_usr_guess = get_user_guess()
        if check_win(number_to_guess, curr_usr_guess) is True:
            print("You have guessed all 4 numbers in ",
                  attempt_count, " attempts !!!")
            break
        else:
            cow_count = check_cows(number_to_guess, curr_usr_guess)
            bull_count = check_bulls(number_to_guess, curr_usr_guess)
            print("You have ", cow_count, " cows, ", bull_count,
                  " bulls ", attempt_count, " attempts tryed")
        attempt_count += 1

    if attempt_count == max_attempt_count:
        print("You have lost game guess count is more than 20 ... ")


if __name__ == "__main__":
    main()
