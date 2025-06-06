class Solution(object):
    def robotWithString(self, s):
        """
        :type s: str
        :rtype: str
        """
        f = [0] * 26
        
        for c in s:
            f[ord(c) - ord('a')] += 1
        
        p = []
        t = []
        
        def getMin():
            for i in range(26):
                if f[i] > 0:
                    return chr(i + ord('a'))
            
            return 'z'
        
        for c in s:
            t.append(c)
            f[ord(c) - ord('a')] -= 1
            
            while t and t[-1] <= getMin():
                p.append(t.pop())
        
        while t:
            p.append(t.pop())
        
        return "".join(p)

obj = Solution()
print(obj.robotWithString("bydizfve"))