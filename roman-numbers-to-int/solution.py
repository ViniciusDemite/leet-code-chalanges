import re


class Solution:
    def __init__(self):
        self._roman_numbers = {
          'M': 1000,
          'D': 500,
          'C': 100,
          'L': 50,
          'X': 10,
          'V': 5,
          'I': 1
        }

    def romanToInt(self, s: str) -> int:
        assert isinstance(s, str), 'O valor passado deve ser uma string'

        if self._validate_received_string(s):
            raise ValueError('A formatação do valor está errada, por favor verifique o valor informado')

        total = 0
        received_roman_number_length = len(s)

        for index, letter in enumerate(s):
            if index + 1 != received_roman_number_length and self._roman_numbers[s[index + 1]] > self._roman_numbers[letter]:
                total -= self._roman_numbers[letter]
                continue

            total += self._roman_numbers[letter]

        return total

    @staticmethod
    def _validate_received_string(s: str) -> bool:
        string_length = len(s)
        regexp = re.compile(r'([^MDCLXVI])\w+')
        
        return (string_length == 0 or string_length > 15) or regexp.search(s)