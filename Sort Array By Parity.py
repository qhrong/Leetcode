class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return(sorted([x for x in A if x % 2 == 0]) +
        sorted([x for x in A if x % 2 != 0]))