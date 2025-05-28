from collections import defaultdict

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        maxLen = 0
        windowLen = 0
        window = defaultdict(int)
        
        for right in range(len(s)):
            window[s[right]] += 1
            windowLen += 1
            
            while windowLen - max(window.values()) > k:
                windowLen -= 1
                window[s[left]] -= 1
                left += 1
            
            maxLen = max(maxLen, windowLen)
        
        return maxLen

obj = Solution()
print(obj.characterReplacement("AABABBA", 1))