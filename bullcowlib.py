import random


def gen_random_ints() -> list:
    """Function generates 4 random non-repeating single digit list

    Args:
        none

    Returns:
        numbers: with 4 integers in range 0-9
    """
    numbers = []
    while len(numbers) < 4:
        number = random.randrange(0, 9)
        if number not in numbers:
            numbers.append(number)
    return numbers


def get_user_guess() -> str:
    """Function collects 4 digit string from stdin

    Args:
        none

    Returns:
        user_guess: 4 digit string

    Rise exception:
         # Validation #1 for exact len of 4 : will catch if not equal 4 len
         # Validation #2 for is numeric : will catch if entered value is not int
    """
    required_len = 4
    input_is_valid = False
    while input_is_valid is False:
        user_guess = input("\nEnter 4 numbers:")
        # Validation #1 and #2 for exact len of 4 and is numeric Ture
        if len(user_guess) == required_len and user_guess.isnumeric():
            input_is_valid = True
            return user_guess
        else:
            print(
                "Entered value is more or less than 4 numbers or does not contain 4 numbers please try again. ")


def check_win(number_to_guess: list, ug: str) -> bool:
    """Function validates condition if user guessed 4 cows
       from rules of game it leads to  end of game and user win
    """
    if check_cows(number_to_guess, ug) == 4:
        return True


def check_cows(number_to_guess: list, ug: str) -> int:
    """Function compares user guess string with guess list and counts and return cow count

    Args:
        number_to_guess: list of single digit ints
        ug: str of 4 number digit

    Returns:
        cow_count: int
    """
    cow_count = 0
    for idx in range(len(number_to_guess)):
        if number_to_guess[idx] == int(ug[idx]):
            cow_count += 1
    return cow_count


def check_bulls(number_to_guess: list, ug: str) -> int:
    """Function compares user guess with guess list and counts and return bulll count

    Args:
        number_to_guess: list of single digit ints
        ug: str of 4 number digit

    Returns:
        bull_count: int
    """
    bull_count = 0
    for idx in range(len(number_to_guess)):
        if number_to_guess[idx] != int(ug[idx]) and (int(ug[idx]) in number_to_guess):
            bull_count += 1
    return bull_count


def pritty_print(memory_list: list) -> None:
    """ Function iterates obver historic guess number results
    and prints in one line and  enumerates number of lines 
    """
    memory_lines = int(len(memory_list) / 3)
    last_index = memory_lines * 3
    for index in range(3, last_index + 1, 3):

        line_number = str(int(index / 3))
        guess_num_str = memory_list[index - 3]
        cow_str = memory_list[index - 1]
        bull_str = memory_list[index - 2]
        print(line_number, guess_num_str, cow_str, bull_str)


def memorize_guesses(cug: str, bc: int, cc: int, memory: list) -> list:
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
    memory.append(cug)
    memory.append(cc_str)
    memory.append(bc_str)
    return memory
