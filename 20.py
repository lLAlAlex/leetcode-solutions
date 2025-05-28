class Solution(object):
    def isValid(self, s):           
        stack = []
        
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif c == ')':
                if not stack or stack.pop() != '(':
                    return False
            elif c == '}':
                if not stack or stack.pop() != '{':
                    return False
            elif c == ']':
                if not stack or stack.pop() != '[':
                    return False
            
        return not stack

obj = Solution()
print(obj.isValid('[]'))