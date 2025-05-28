class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        newStr = []
        
        for i, char in enumerate(s):
            if s[i].isdigit():
                newStr.pop()
            else:
                newStr.append(char)
        
        return ''.join(newStr)

obj = Solution()
print(obj.clearDigits("abc"))