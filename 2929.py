class Solution(object):
    def distributeCandies(self, n, limit):
        """
        :type n: int
        :type limit: int
        :rtype: int
        """
        ans = 0
        
        for i in range(min(limit, n) + 1):
            if n - i > 2 * limit:
                continue
            ans += min(limit, n - i) - max(0, n - i - limit) + 1
        
        return ans

obj = Solution()
print(obj.distributeCandies(3, 3))