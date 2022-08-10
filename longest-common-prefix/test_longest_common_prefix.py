import unittest
import string
import random
from solution import Solution


class TestLongestCommonPrefix(unittest.TestCase):
  def test_longest_common_prefix_raises_assertion_error_for_not_receiving_a_list(self):
    with self.assertRaises(AssertionError):
      solution = Solution()
      solution.longestCommonPrefix('test')

  def test_longest_common_prefix_raises_assertion_error_for_list_with_item_different_than_string(self):
    with self.assertRaises(AssertionError):
      solution = Solution()
      solution.longestCommonPrefix(['test', 52])

  def test_longest_common_prefix_raises_value_error_for_empty_list(self):
    with self.assertRaises(ValueError):
      solution = Solution()
      solution.longestCommonPrefix([])

  def test_longest_common_prefix_raises_value_error_for_list_with_empty_string_as_an_item(self):
    with self.assertRaises(ValueError):
      solution = Solution()
      solution.longestCommonPrefix(['test', ''])

  def test_longest_common_prefix_raises_value_error_for_list_with_more_than_200_items(self):
    word = ''.join(random.choice(string.ascii_lowercase))

    with self.assertRaises(ValueError):
      solution = Solution()
      solution.longestCommonPrefix([word for _ in range(201)])

  def test_longest_common_prefix_raises_value_error_for_list_with_word_that_has_more_than_200_chars(self):
    word = ''.join(random.choices(string.ascii_lowercase, k=201))

    with self.assertRaises(ValueError):
      solution = Solution()
      solution.longestCommonPrefix(['test', word])

  def test_longest_common_prefix_returns_fl_str(self):
    solution = Solution()
    common_prefix = solution.longestCommonPrefix(["flower", "flow", "flight"])

    self.assertEqual(common_prefix, 'fl')

  def test_longest_common_prefix_returns_empty_str(self):
    solution = Solution()
    common_prefix = solution.longestCommonPrefix(["dog", "racecar", "car"])

    self.assertEqual(common_prefix, '')

  def test_longest_common_prefix_returns_d_str(self):
    solution = Solution()
    common_prefix = solution.longestCommonPrefix(["drawn", "dog", "dodge"])

    self.assertEqual(common_prefix, 'd')

  def test_longest_common_prefix_returns_empty_str_for_words_with_common_suffixes(self):
    solution = Solution()
    common_prefix = solution.longestCommonPrefix(
      ["impact", "pact", "paction", "pactum"]
    )

    self.assertEqual(common_prefix, '')

  def test_longest_common_prefix_returns_lee_str(self):
    solution = Solution()
    common_prefix = solution.longestCommonPrefix(["leets", "leetcode", "leet", "leeds"])

    self.assertEqual(common_prefix, 'lee')


if __name__ == '__main__':
  unittest.main(verbosity=2)