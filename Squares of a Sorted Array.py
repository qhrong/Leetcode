class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:

        res = [0] * len(A)

        left, right = 0, len(A) - 1

        for i in range(len(A) - 1, -1, -1):
            if abs(A[left]) > abs(A[right]):
                res[i] = A[left] ** 2
                left += 1
            else:
                res[i] = A[right] ** 2
                right -= 1

        return (res)
# ----------------------------------------------------------------------------------------------------------------------
    class Solution:
        def sortedSquares(self, A: List[int]) -> List[int]:

            # Two pointers:
            # One pointer for negative part
            # One pointer for positive part

            N = len(A)
            j = 0

            while j < N and A[j] < 0:
                j += 1

            i = j - 1

            res = []
            while i >= 0 and j < N:
                if A[i] ** 2 < A[j] ** 2:
                    res.append(A[i] ** 2)
                    i -= 1
                else:
                    res.append(A[j] ** 2)
                    j += 1

            # If i or j didn't finish
            while i >= 0:
                res.append(A[i] ** 2)
                i -= 1
            while j < N:
                res.append(A[j] ** 2)
                j += 1

            return res