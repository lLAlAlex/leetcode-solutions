class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        
        maxCandy = min(candies)
        
        i = 0
        
        while candies.count(maxCandy) < k:
            target = candies[i] - maxCandy
            
            if target > 0:
                candies[i] = target
                candies.append(maxCandy)
            
            if candies.count(maxCandy) == k:
                return maxCandy
            
            i += 1
        
        return 0

obj = Solution()
print(obj.maximumCandies([4, 7, 5], 4))