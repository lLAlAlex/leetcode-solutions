class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def count(prefix, n):
            steps = 0
            curr = prefix
            next = prefix + 1
            
            while curr <= n:
                steps += min(n + 1, next) - curr
                curr *= 10
                next *= 10
            return steps
        
        curr = 1
        k -= 1
        
        while k > 0:
            steps = count(curr, n)
            
            if steps <= k:
                k -= steps
                curr += 1
            else:
                curr *= 10
                k -= 1
        
        return curr

obj = Solution()
print(obj.findKthNumber(13, 2))