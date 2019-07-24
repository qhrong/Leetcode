class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) > 0:
            count = nums.count(0)
            nums[:] = (i for i in nums if i != 0)
            nums.extend([0] * count)  # use extend instead of append
