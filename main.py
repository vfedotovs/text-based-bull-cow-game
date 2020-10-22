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

def pritty_print(memory_list: list) -> None:
    # print("debug: mylist len:", len(mylist))
    memory_lines = int(len(memory_list) / 3)  # float
    last_index = memory_lines * 3
    #for lines in range(myrange):
    for i in range(3, last_index + 1 , 3):

        line_number = str(int(i / 3))
        guess_num_str = memory_list[i - 3]
        cow_str = memory_list[i - 2]
        bull_str = memory_list[i - 1]

        print(line_number, guess_num_str, cow_str, bull_str)


def memorize_guesses(cug: str,bc :int,cc :int, mylist: list) ->list:
    """Function converts variables to strings and appends to list

    Parameters:
    cug -> curr_usr_guess str
    bc ->  bull_count int
    cc ->  cow_count int
    mylist -> previous guess history as list

    Returns: mylist as list
    """
    bc_str = "bulls: " + str(bc)
    cc_str = "cows: " + str(cc)
    mylist.append(cug)
    mylist.append(cc_str)
    mylist.append(bc_str)
    return mylist


def main():
    print(game_rules)
    number_to_guess = gen_random_ints()
    attempt_count = 1
    max_attempt_count = 20
    pritty_list = []
    while attempt_count < max_attempt_count:
        curr_usr_guess = get_user_guess()
        if check_win(number_to_guess, curr_usr_guess) is True:
            print("You have guessed all 4 numbers in ",
                  attempt_count, " attempts !!!")
            break
        else:
            cow_count = check_cows(number_to_guess, curr_usr_guess)
            bull_count = check_bulls(number_to_guess, curr_usr_guess)
            #print("You have ", cow_count, " cows, ", bull_count,
            #      " bulls ", attempt_count, " attempts tryed")
            #print("---test ---")
            guess_history = memorize_guesses(curr_usr_guess, cow_count, bull_count, pritty_list)
            pritty_print(guess_history)

        attempt_count += 1

    if attempt_count == max_attempt_count:
        print("You have lost game guess count is more than 20 ... ")


if __name__ == "__main__":
    main()
