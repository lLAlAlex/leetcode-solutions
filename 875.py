import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        low = 1
        high = max(piles)
        mid = 0
        
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            spd = 0
            
            for p in piles:
                spd += math.ceil(float(p) / mid)
            
            if spd <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans

obj = Solution()
print(obj.minEatingSpeed([3,6,7,11], 8))