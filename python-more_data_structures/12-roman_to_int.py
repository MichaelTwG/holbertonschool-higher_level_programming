#!/usr/bin/pyhon3
def roman_to_int(roman_string):
    result = 0
    if type(roman_string) != str or roman_string is None:
        return 0
    roman_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}
    for i in range(0, len(roman_string)):
        if i < len(roman_string) - 1:
            if roman_dic[roman_string[i]] < roman_dic[roman_string[i + 1]]:
                result -= roman_dic[roman_string[i]]
            else:
                result += roman_dic[roman_string[i]]
        else:
            result += roman_dic[roman_string[i]]
    return result
