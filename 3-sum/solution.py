from typing import List
from itertools import combinations


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        assert len(nums) >= 3 and len(nums) <= 3000, 'É necessário ter mais de 3 números na lista!!'
        assert all(isinstance(number, int) for number in nums), 'Todos os elementos da lista devem ser um inteiro'

        triplets: List[List[int]] = []

        for index in range(0, len(nums)):
          combination: List[int] = []
          n1 = nums[index]

          if n1 != nums[index + 1] and n1 != nums[index + 2]:
            combination.append(n1)

          if sum(combination) == 0:
            triplets.append(combination)

        # combined_nums = combinations(nums, 3)

        # for combination in combined_nums:
        #   if sum([number for number in combination]) == 0:
        #     triplets.append(list(combination))

        return triplets