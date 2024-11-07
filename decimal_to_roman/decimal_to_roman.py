decimal_to_roman_pairs = [
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I')
]

def convert_decimal_to_roman(number):
    result = ""
    for decimal, roman in decimal_to_roman_pairs:
        while number >= decimal:
            number -= decimal
            result += roman
    return result

if __name__ == '__main__':
    assert convert_decimal_to_roman(1) == 'I'
    assert convert_decimal_to_roman(2) == 'II'
    assert convert_decimal_to_roman(4) == 'IV'
    assert convert_decimal_to_roman(5) == 'V'
    assert convert_decimal_to_roman(6) == 'VI'
    assert convert_decimal_to_roman(7) == 'VII'
    assert convert_decimal_to_roman(10) == 'X'
    assert convert_decimal_to_roman(34) == 'XXXIV'
    assert convert_decimal_to_roman(256) == 'CCLVI'
    assert convert_decimal_to_roman(516) == 'DXVI'
    assert convert_decimal_to_roman(1234) == 'MCCXXXIV'
    print('Test passed!')