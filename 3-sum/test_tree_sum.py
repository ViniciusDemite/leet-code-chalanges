import unittest
from solution import Solution


class TestTreeSum(unittest.TestCase):
  def test_tree_sum_assert_nums_length_minimum_3(self):
    with self.assertRaises(AssertionError):
      solution = Solution()
      solution.threeSum([1, 2])

  def test_tree_sum_assert_nums_length_maximum_3000(self):
    with self.assertRaises(AssertionError):
      solution = Solution()
      solution.threeSum([number for number in range(0, 3002)])

  def test_tree_sum_assert_nums_items_are_all_integers(self):
    with self.assertRaises(AssertionError):
      solution = Solution()
      solution.threeSum([1, 2, 3, '4', (5, 5)])

  def test_tree_sum_returns_empty_list(self):
    solution = Solution()
    sums = [0, 1, 1]

    self.assertEqual(solution.threeSum(sums), [])

  def test_tree_sum_returns_two_triplets(self):
    solution = Solution()
    sums = [-1, 0, 1, 2, -1, -4]

    self.assertEqual(solution.threeSum(sums), [[-1, -1, 2], [-1, 0, 1]])

  def test_tree_sum_returns_single_triplet_of_zeros(self):
    solution = Solution()
    sums = [0,0,0]

    self.assertEqual(solution.threeSum(sums), [[0, 0, 0]])


if __name__ == '__main__':
  unittest.main(verbosity=2)