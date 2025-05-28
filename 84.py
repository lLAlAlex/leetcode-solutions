class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        maxArea = 0
        
        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1] > height:
                i, h = stack.pop()
                maxArea = max(maxArea, h * (index - i))
                start = i
            
            stack.append((start, height))
            # print(stack)
        
        for s in stack:
            maxArea = max(maxArea, s[1] * (len(heights) - s[0]))
        
        return maxArea

obj = Solution()
print(obj.largestRectangleArea([2,1,5,6,2,3]))