class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even, odd = 0, 1
        res = [0] * len(A)

        for ele in A:
            if ele % 2 == 0:
                res[even] = ele
                even += 2
            else:
                res[odd] = ele
                odd += 2
        return (res)