class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        res = []
        
        for i in range(len(words)):
            c = words[i]
            if x in c:
               res.append(i)
            
        return res

obj = Solution()
obj.findWordsContaining(["leet", "code"], "x")