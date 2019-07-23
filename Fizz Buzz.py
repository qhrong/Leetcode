class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []

        for num in range(1, n + 1):

            divi_by_3 = (num % 3 == 0)
            divi_by_5 = (num % 5 == 0)

            num_ans = ""  # store the string for each num

            if divi_by_3:
                num_ans += 'Fizz'
            if divi_by_5:
                num_ans += 'Buzz'
            if not num_ans:  # not divisible by 3 or 5
                num_ans = str(num)

            res.append(num_ans)
        return res