class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      for idx1, item in enumerate(nums):
        diff = (target - item)
        for idx2, digit in enumerate(nums):
            if digit == diff and idx1 != idx2:
                res = [idx2, idx1]
                res.sort()
                return res





