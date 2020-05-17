import random


def gen_random_ints() -> list:
    """Function generates 4 random non-repeating single digit list

    Args:
        none

    Returns:
        number_list: with 4 integers in range 0-9
    """
    number_list = []
    while len(number_list) < 4:
        number = random.randrange(0, 9)
        if number not in number_list:
            number_list.append(number)
    return number_list
