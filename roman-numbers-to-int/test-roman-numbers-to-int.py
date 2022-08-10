import unittest
from solution import Solution


class TestRomanNumberToInt(unittest.TestCase):
  def test_roman_number_to_int_raises_assertion_error_if_values_is_not_a_string(self):
    with self.assertRaises(AssertionError):
      solution = Solution()
      solution.romanToInt(125)

  def test_roman_number_to_int_raises_value_error_if_values_has_invalid_input_values(self):
    with self.assertRaises(ValueError):
      solution = Solution()
      solution.romanToInt('AGV1226')

  def test_roman_number_to_int_raises_value_error_if_values_has_invalid_length(self):
    with self.assertRaises(ValueError):
      solution = Solution()
      solution.romanToInt('a15fdsf6dsf65dsaf6ds54fads')

  def test_roman_number_to_int_raises_value_error_param_is_empty(self):
    with self.assertRaises(ValueError):
      solution = Solution()
      solution.romanToInt('')

  def test_roman_number_to_int_returns_3_for_input_III(self):
    solution = Solution()
    self.assertEqual(solution.romanToInt('III'), 3)

  def test_roman_number_to_int_returns_58_for_input_LVIII(self):
    solution = Solution()
    self.assertEqual(solution.romanToInt('LVIII'), 58)

  def test_roman_number_to_int_returns_1994_for_input_MCMXCIV(self):
    solution = Solution()
    self.assertEqual(solution.romanToInt('MCMXCIV'), 1994)

  def test_roman_number_to_int_returns_27_for_input_XXVII(self):
    solution = Solution()
    self.assertEqual(solution.romanToInt('XXVII'), 27)

if __name__ == '__main__':
    unittest.main(verbosity=2)
