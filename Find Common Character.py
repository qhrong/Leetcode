class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        check = list(A[0])
        for word in A:
            newCheck = []
            for c in word:
                if c in check:
                    newCheck.append(c #if c exists, append in the storing list
                    check.remove(c) #and then, remove from check so that the following loop can only search on the list of of common characters
            check = newCheck

        return check