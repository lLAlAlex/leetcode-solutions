from collections import defaultdict

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        maxLen = 0
        d = defaultdict(str)
        
        for right in range(len(s)):
            if s[right] in d and d[s[right]] >= left:
                left = d[s[right]] + 1
                
            d[s[right]] = right
            maxLen = max(maxLen, right - left + 1)
        
        return maxLen

obj = Solution()
print(obj.lengthOfLongestSubstring("abba"))