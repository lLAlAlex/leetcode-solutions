from collections import defaultdict

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        left = 0
        k = 10
        curr = defaultdict()
        ans = []
        
        for i in range(len(s) - k + 1):
            currStr = s[i:i+10]
              
            if curr.get(currStr) != None:
                ans.append(currStr)
                
            curr[currStr] = i
            
        return list(set(ans))

obj = Solution()
print(obj.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))