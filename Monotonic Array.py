class Solution:
    def isMonotonic(self, A: List[int]) -> bool:

    # First method
        decreasing = increasing = True

        for i in range(1, len(A)):
            if A[i - 1] > A[i]:
                decreasing = False
            if A[i - 1] < A[i]:
                increasing = False

        return decreasing or increasing

    #Second method

        return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or all(A[i] >= A[i + 1] for i in range(len(A) - 1)))