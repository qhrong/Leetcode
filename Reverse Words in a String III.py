class Solution:
    def reverseWords(self, s: str) -> str:
        A = s.split(' ')
        reverse = []
        for i in A:
            reverse.append(i[::-1])
        return ' '.join(reverse)