class Solution:
    # O(n) Naive method
    def fixedPoint(self, A: List[int]) -> int:
        for i in range(len(A)):
            if A[i] == i:
                return i
        return -1


     # Binary Search -- Iteration
    def fixedPoint(self, A: List[int]) -> int:
        low = 0
        high = len(A) - 1

        while high >= low:

            mid = (low + high) // 2 # mid point needs to be updated

            if A[mid] == mid:
                return mid
            elif A[mid] < mid:
                low = mid + 1
            else:
                high = mid - 1
        return -1