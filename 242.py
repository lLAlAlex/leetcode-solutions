from collections import Counter

class Solution:
    def validate(self, s, t):
        if len(s) == len(t):
            if Counter(s) == Counter(t):
                return True
        return False

    def isAnagram(self, s: str, t: str):
        return self.validate(s, t)
    
# obj = Solution()
# obj.isAnagram("racecar", "carrace")