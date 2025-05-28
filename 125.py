class Solution(object):
    # def isPalindrome(self, s):
    #     res = ''.join(word for word in s if word.isalnum()).lower()
    #     left = ''
    #     right = ''
        
    #     for i in range(len(res) // 2):
    #         left += res[i]
        
    #     if len(res) % 2 == 0:
    #         for i in range(len(res)-1, len(res) // 2 - 1, -1):
    #             right += res[i]
    #     else:
    #         for i in range(len(res)-1, len(res) // 2, -1):
    #             right += res[i]
        
    #     return left == right
    
    # def isPalindrome(self, s):
    #     newStr = ''
    #     for word in s:
    #         if word.isalnum():
    #             newStr += word.lower()
        
    #     return newStr == newStr[::-1]
    
    def isPalindrome(self, s):
        res = ''.join(word for word in s if word.isalnum()).lower()
        
        return res == res[::-1]

obj = Solution()
print(obj.isPalindrome("Was it a car or a cat I saw?"))