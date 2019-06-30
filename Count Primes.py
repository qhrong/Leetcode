# n is not included
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        is_prime = [False, False] + [True] * (n - 2)

        for p in range(2, n):

            if is_prime[p]:
                is_prime[p] = True

                for i in range(p * 2, n, p):
                    is_prime[i] = False

        return (sum(is_prime))