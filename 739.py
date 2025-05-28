class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        res = [0] * len(temperatures)
        
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev = stack.pop()
                res[prev] = i - prev
            
            stack.append(i)
        
        return res
                
obj = Solution()
print(obj.dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))