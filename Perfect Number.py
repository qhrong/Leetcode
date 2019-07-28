class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 0:
            return False

        res = 0

        for i in range(1, int(num ** 0.5) + 1):  # range needs one more
            if num % i == 0:
                res += i

                if i * i != num: # the complementary side, so no need to go the other sqrt side
                    res += num / i

        return res - num == num