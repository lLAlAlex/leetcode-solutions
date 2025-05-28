class Solution:
    def generateParenthesis(self, n):
        stack = []
        res = []
        
        def helper(openCount, closeCount):
            if openCount == closeCount == n:
                res.append("".join(stack))
                return
            
            if openCount < n:
                stack.append("(")
                helper(openCount + 1, closeCount)
                stack.pop()
            
            if closeCount < openCount:
                stack.append(")")
                helper(openCount, closeCount + 1)
                stack.pop()
            
        helper(0, 0)
        return res

obj = Solution()
print(obj.generateParenthesis(3))