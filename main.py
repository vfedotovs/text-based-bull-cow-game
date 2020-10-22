import bullcow_lib


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
    number_to_guess = bullcow_lib.gen_random_ints()
    attempt_count = 1
    max_attempt_count = 20
    pritty_list = []
    while attempt_count < max_attempt_count:
        curr_usr_guess = bullcow_lib.get_user_guess()
        if bullcow_lib.check_win(number_to_guess, curr_usr_guess) is True:
            print("You have guessed all 4 numbers in ",
                  attempt_count, " attempts !!!")
            break
        else:
            cow_count = bullcow_lib.check_cows(number_to_guess, curr_usr_guess)
            bull_count = bullcow_lib.check_bulls(number_to_guess, curr_usr_guess)
            guess_history = bullcow_lib.memorize_guesses(
                curr_usr_guess, bull_count, cow_count, pritty_list)
            bullcow_lib.pritty_print(guess_history)

        attempt_count += 1

    if attempt_count == max_attempt_count:
        print("You have lost game guess count is more than 20 ... ")


if __name__ == "__main__":
    main()
