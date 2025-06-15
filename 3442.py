from collections import Counter

class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        oddMax = 0
        evenMin = 1000
        
        hm = Counter(s)
        chars = set(s)
        
        for c in chars:
            if hm[c] % 2 == 0:
                evenMin = min(evenMin, hm[c])
            else:
                oddMax = max(oddMax, hm[c])
        
        return oddMax - evenMin

obj = Solution()
print(obj.maxDifference("mmsmsym"))