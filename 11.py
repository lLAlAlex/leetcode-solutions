class Solution:
    def maxArea(self, heights):
        i = 0
        j = len(heights) - 1
        maxHeight = 0
        
        while i != j:
            maxHeight = max(maxHeight, min(heights[i], heights[j]) * (j - i))
            
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        return maxHeight

obj = Solution()
print(obj.maxArea([8,7,2,1]))