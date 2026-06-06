class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        res = []
        for num in nums:
            if num != 0:
                prod *= num
        for i, num in enumerate(nums):
            num_of_zeros = nums.count(0)
            if (num_of_zeros > 1) or (num_of_zeros == 1 and num != 0):
                res.append(0)
            elif num_of_zeros == 1 and num == 0:
                res.append(prod)
            else:
                res.append(prod//num)
        return res




        