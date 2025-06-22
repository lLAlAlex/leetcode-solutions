class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        ans = []
        
        for i in range(k-1, len(s), k):
            ans.append(s[i-(k-1):i+1])
        
        remaining = len(s) % k
        
        if remaining:
            temp = ""
            for c in s[-remaining:len(s)]:
                temp += c
            
            for _ in range(k - remaining):
                temp += fill
            
            ans.append(temp)
        
        return ans

obj = Solution()
print(obj.divideString("abcdefghij", 3, "x"))