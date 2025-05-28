class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        str1Len = len(str1)
        str2Len = len(str2)
        
        prevRow = [str2[0:col] * col for col in range(str2Len + 1)]
        
        for row in range(1, str1Len + 1):
            currRow = [str1[0:row]] + [None for _ in range(str2Len)]
            
            for col in range(1, str2Len + 1):
                if str1[row - 1] == str2[col - 1]:
                    currRow[col] = prevRow[col - 1] + str1[row - 1]
                else:
                    s1 = prevRow[col]
                    s2 = currRow[col - 1]
                    
                    currRow[col] = (
                        s1 + str1[row - 1]
                        if len(s1) < len(s2)
                        else s2 + str1[col - 1]
                    )
            prevRow = currRow
        
        return prevRow

obj = Solution()
print(obj.shortestCommonSupersequence("abac", "cab"))