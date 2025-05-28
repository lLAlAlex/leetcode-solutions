class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        newStr = s
        startIndex = newStr.find(part)
        
        while startIndex != -1:
            newStr = newStr[:startIndex] + newStr[startIndex+len(part):]
            startIndex = newStr.find(part)
            
        return newStr

obj = Solution()
print(obj.removeOccurrences("daabcbaabcbc", "abc"))