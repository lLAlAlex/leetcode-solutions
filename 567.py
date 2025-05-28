from collections import Counter

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s2) < len(s1):
            return False
        
        s1Freq = Counter(s1)
        windowFreq = Counter(s2[:len(s1)])
        
        if s1Freq == windowFreq:
            return True
        
        left = 0
        
        for right in range(len(s1), len(s2)):
            windowFreq[s2[right]] += 1
            windowFreq[s2[left]] -= 1
            
            if windowFreq[s2[left]] == 0:
                del windowFreq[s2[left]]
            left += 1
            
            if windowFreq == s1Freq:
                return True
        
        return False
        
obj = Solution()
print(obj.checkInclusion("ab", "eidbaooo"))