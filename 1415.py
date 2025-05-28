class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        
        # 2
        # ab, ba, ac, ca, bc, cb
        letters = ['a', 'b', 'c']
        index = 0
        stack = [""]
        
        while stack:
            curr = stack.pop()
            
            if len(curr) == n:
                index += 1
                
                if index == k:
                    return curr
                continue
            
            for char in reversed(letters):
                if len(curr) == 0 or curr[-1] != char:
                    stack.append(curr+char)
        
        return ""

obj = Solution()
print(obj.getHappyString(2, 6)) 