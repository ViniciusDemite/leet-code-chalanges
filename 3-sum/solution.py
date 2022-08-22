from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        assert len(nums) >= 3 and len(nums) <= 3000, 'É necessário ter mais de 3 números na lista!!'
        assert all(isinstance(number, int) for number in nums), 'Todos os elementos da lista devem ser um inteiro'

        nums.sort()
        triplets: List[List[int]] = []
        nums_len = len(nums)

        for n1_index in range(nums_len - 2):
          if n1_index > 0 and nums[n1_index] == nums[n1_index - 1]:
            continue

          (n2_index, n3_index) = (n1_index + 1, nums_len - 1)

          while n2_index < n3_index:
            triplet_sum = nums[n1_index] + nums[n2_index] + nums[n3_index]

            if triplet_sum == 0:
              triplets.append([
                nums[n1_index], nums[n2_index], nums[n3_index]
              ])

              n3_index -= 1

              while n2_index < n3_index and \
              nums[n3_index] == nums[n3_index + 1]:
                n3_index -= 1
            elif triplet_sum > 0:
              n3_index -= 1
            else:
              n2_index += 1

        return triplets