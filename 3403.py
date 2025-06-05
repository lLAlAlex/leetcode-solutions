class Solution(object):
    def answerString(self, word, numFriends):
        """
        :type word: str
        :type numFriends: int
        :rtype: str
        """
        if numFriends == 1:
            return word
        
        largestChar = max(word)
        
        if numFriends == len(word):
            return largestChar
        
        ans = ""
        # l = 0
        n = len(word)
        maxLen = n - numFriends + 1
        
        for i, c in enumerate(word):
            if c == largestChar:
                possible = word[i:i+maxLen]
                
                ans = max(ans, possible)

        return ans
        
        # for r in range(n):
        #     ans = max(ans, word[l:r+1])
        #     # print(word[l:r+1])
            
        #     if len(word[l:r+1]) >= n - numFriends + 1:
        #         # while len(word[l:r+1]) > 1 and l <= r + 1:
        #         temp = word[l:r+1]
        #         ans = max(ans, word[l:r+1])
        #         l += 1
                
        #         left = 0
        #         while len(temp) > 1 and left <= len(temp):
        #             ans = max(ans, temp[left:len(temp)])
        #             # print(temp[left:len(temp)])
        #             left += 1

obj = Solution()
print(obj.answerString("epbbppl", 2))