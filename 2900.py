class Solution(object):
    def getLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        sign = None
        res = []
        
        for i in range(len(words)):
            if sign != groups[i] or sign == None:
                res.append(words[i])
            sign = groups[i]
            
        return res
                
obj = Solution()
print(obj.getLongestSubsequence(["a","b","c","d"], [1,0,1,1]))