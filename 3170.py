class Solution(object):
    def clearStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = [[] for _ in range(26)]
        ans = list(s)
        
        for i, c in enumerate(s):
            if c != '*':
                arr[ord(c) - ord('a')].append(i)
            else:
                for j in range(26):
                    if arr[j]:
                        last = arr[j].pop()
                        ans[last] = "*"
                        break
        
        return "".join(c for c in ans if c != '*')
    
obj = Solution()
print(obj.clearStars("aaba*"))