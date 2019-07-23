class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        not_duplicate = []
        for i in nums:
            if i not in not_duplicate:
                not_duplicate.append(i)
            else:
                not_duplicate.remove(i) #remove duplicate
        return not_duplicate.pop() #return number not list