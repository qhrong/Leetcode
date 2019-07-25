class Solution:
    def addDigits(self, num: int) -> int:

        while num >= 10:  # end when only one digit

            tmp = 0

            while num > 0:
                tmp += num % 10
                num //= 10

            num = tmp

        return num
