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
