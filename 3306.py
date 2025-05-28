class Solution(object):
    def countOfSubstrings(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        res = []
        temp = ""
        consonant = ""
        
        for i in range(len(word)):
            if word[i] in vowels and word[i] not in temp:
                temp += word[i]
            
            if word[i] not in vowels:
                consonant = word[i]
            
            if consonant != "" and len(temp) == 5:
                res.append(temp + consonant)
                temp = ""
                consonant = ""
            
        return res
            
obj = Solution()
print(obj.countOfSubstrings("ieaouqqieaouqq", 1))