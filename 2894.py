class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        sum1 = 0
        sum2 = 0
        
        for i in range(n+1):
            if i % m != 0:
                sum1 += i
            else:
                sum2 += i
        
        res = sum1 - sum2
        
        return res

obj = Solution()
print(obj.differenceOfSums(10, 3))