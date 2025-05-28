class Solution(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n == 1:
        #     return 1
        
        # denominator = 4
        # res = 1
        
        # for i in range(1, n + 1):
        #     if i != 1:
        #         res += denominator
        #         denominator += 4
        
        return n**2 + (n - 1)**2

obj = Solution()
print(obj.coloredCells(4))