class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        ans = ['a']
        
        while len(ans) < k:
            temp = []
            for c in ans:
                if c == 'z':
                    temp.append('a')
                else:
                    temp.append(chr(ord(c) + 1))
            ans += temp
        
        return ans[k-1]
    
obj = Solution()
print(obj.kthCharacter(5))