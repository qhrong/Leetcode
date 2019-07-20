class Solution:
    def toLowerCase(self, str: str) -> str:
        res=[]
        for i in str:
            if 65 <= ord(i) <= 90:
                res.append(chr(ord(i)+32))
            else:
                res.append(i)
        return ''.join(res)