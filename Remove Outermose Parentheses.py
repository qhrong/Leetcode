class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res = []
        balance = 0
        j = 0

        for i in range(len(S)):
            if S[i] == '(':
                balance += 1
            elif S[i] == ')':
                balance -= 1
            if balance == 0:
                res.append(S[j + 1:i])
                j = i + 1  # next set of parentheses

        return ''.join(res)