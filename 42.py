class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        
        l, r = 0, n - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        
        while l < r:
            # print(f"Left: {leftMax}")
            # print(f"Right: {rightMax}")
            
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
            
            # print(f"Result: {res}")
        
        return res

obj = Solution()
print(obj.trap([0,2,0,3,1,0,1,3,2,1]))