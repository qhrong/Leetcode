class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:

        # the idea is to sort the array
        nums = sorted(nums)

        res = 0
        for i in range(len(nums)):
            if i % 2 == 0:  # min can only be the even ones
                res += nums[i]
            else:
                next
        return res