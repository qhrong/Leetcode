class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        left = 0
        right = len(nums) - 1

        if target not in nums:
            return [-1, -1]

        while left < right and left < len(nums) - 1 and right > 0:
            if nums[left] != target:
                left += 1
            if nums[right] != target:
                right -= 1
            if nums[left] == target and nums[right] == target:
                break

        return left, right
