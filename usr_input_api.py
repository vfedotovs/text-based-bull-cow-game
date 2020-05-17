def get_user_guess() -> str:
    """Function collects 4 digit string from stdin

    Args:
        none

    Returns:
        user_guess: 4 digit string

    Rise exception:
         # Validation #1 for exact len of 4 : will catch if not equal 4 len
         # Validation #2 for is numeric : will catch if entered value is not number
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
