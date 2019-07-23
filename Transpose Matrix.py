class Solution:

# This method will not work for m*n matrix, only work for m*m
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        return A
# Method two
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        R, C = len(A), len(A[0])
        res = [[None] * R for i in range(C)] #create a matrix for loop
        for r, row in enumerate(A): #enumerate row
            for c, val in enumerate(row): #enumerate column
                res[c][r] = val
        return res