from collections import defaultdict

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        hm = defaultdict(int)
        
        for c in s:
            hm[c] += 1
        
        print(hm)

obj = Solution()
print(obj.romanToInt("MCMXCIV"))