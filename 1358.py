class Solution(object):
    def generateSubstring(self, s, n, index, curr, res):    
        if index == n:
            return
        
        curr += s[index]
        
        if set(curr) >= set(s):
            res.append(curr)
    
        self.generateSubstring(s, n, index + 1, curr, res)
        
        curr = curr[:-1]
        
        if not curr:
            self.generateSubstring(s, n, index + 1, curr, res)
        
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = []
        curr = ""
        
        self.generateSubstring(s, len(s), 0, curr, res)
        
        return len(res)

obj = Solution()
print(obj.numberOfSubstrings("abab"))