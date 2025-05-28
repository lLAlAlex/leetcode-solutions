class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        words = sentence.split()
        
        matches = [word for word in words if word.startswith(searchWord)]
        
        if matches:
            return words.index(matches[0]) + 1
        
        return -1
        
obj = Solution()
print(obj.isPrefixOfWord("i love eating burger", "i"))