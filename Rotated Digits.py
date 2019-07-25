class Solution:
    def rotatedDigits(self, N: int) -> int:
        res = 0
        for x in range(N+1):
            S = str(x)
            if '3' in S or '4' in S or '7' in S:
                continue
            if '2' in S or '5' in S or '6' in S or '9' in S:
                res += 1
        return res