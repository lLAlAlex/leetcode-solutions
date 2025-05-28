from collections import defaultdict, Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        left = 0
        minLen = 9999999
        res = ""
        target = Counter(t)
        window = defaultdict(int)
        have = 0
        need = len(set(t))
        
        # print(target)
        
        for right in range(len(s)):
            window[s[right]] += 1
            
            if window[s[right]] == target[s[right]]:
                # print(right)
                have += 1
                
            while have == need:
                if minLen > right - left + 1:
                    minLen = right - left + 1
                    res = s[left:right+1]
                # print(s[left:right+1])
                if target[s[left]] and window[s[left]] == target[s[left]]:
                    have -= 1
                window[s[left]] -= 1
                left += 1
        
        return res if minLen != 9999999 else ""

obj = Solution()
print(obj.minWindow("aa", "aa"))