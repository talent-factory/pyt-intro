
roman_dictionary = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    'F': 5000,
    'G': 10000,
    'A': 100000
}


# TODO Die Implementation muss noch realisiert werden
# noinspection PyShadowingNames
def not_valid_roman(roman_number):
    """
    Check if a given Roman number is valid or not.

    :param roman_number: The Roman number to be checked.
    :return: True if the Roman number is not valid, False otherwise.

    """
    return False


# noinspection PyShadowingNames
def convert_roman_to_decimal(roman_number: str) -> int:
    """
    Convert a Roman numeral to a decimal number.

    :param roman_number: The Roman numeral to be converted.
    :type roman_number: str
    :return: The decimal value of the Roman numeral.
    :rtype: int
    :raises ValueError: If the Roman numeral is invalid.
    """
    roman_number = roman_number.upper()

    if not_valid_roman(roman_number):
        raise ValueError(f'Invalid roman: {roman_number}')

    decimal = 0
    previous_value = 0  # back tracking

    for char in roman_number:

        if roman_dictionary[char] > previous_value:
            decimal -= previous_value  # decimal = decimal - previous_value
        else:
            decimal += previous_value

        previous_value = roman_dictionary[char]

    decimal += previous_value

    return decimal


if __name__ == '__main__':
    roman_number = input('Bitte geben Sie eine römische Zahl ein: ')

    try:
        decimal_number = convert_roman_to_decimal(roman_number)
        print(decimal_number)
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
