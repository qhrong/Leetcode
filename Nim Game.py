class Solution:
    def canWinNim(self, n: int) -> bool:
        # The idea is that if the number of stones is divisible by 4, impossible to win
        if n % 4 == 0:
            return False
        else:
            return True