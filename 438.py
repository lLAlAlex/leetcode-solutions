from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return []
        
        pFreq = Counter(p)
        windowFreq = Counter(s[:len(p)])
        ans = []
        
        if windowFreq == pFreq:
            ans.append(0)
        
        left = 0
        for right in range(len(p), len(s)):
            windowFreq[s[right]] += 1
            windowFreq[s[left]] -= 1
            
            if windowFreq[s[left]] == 0:
                del windowFreq[s[left]]
            left += 1
            
            if windowFreq == pFreq:
                ans.append(left)
        
        return ans

obj = Solution()
print(obj.findAnagrams("abab", "ab"))