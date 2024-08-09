import roman_numbers as roman

roman_number = input('Bitte gib eine römische Zahl ein: ')

try:
    decimal_number = roman.convert_roman_to_decimal(roman_number)
    print(decimal_number)
except ValueError:
    print('Bitte eine richtige, römische Zahl eingeben.')
