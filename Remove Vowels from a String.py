class Solution:
    def removeVowels(self, S: str) -> str:
        res =[]
        for i in S:
            if i not in 'aeiou':
                res.append(i)
        return ''.join(res)