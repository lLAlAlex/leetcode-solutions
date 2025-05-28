class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        maxList = []
        currWindow = nums[:k]
        
        maxList.append(max(nums[:k]))
        
        for i in range(1, n - k + 1):
            currMax = max(currWindow)
            if currMax > nums[i + k - 1]:
                maxList.append(currMax)
            else:
                maxList.append(nums[i + k - 1])
            
            currWindow.pop(0)
            currWindow.append(nums[i + k - 1])
        
        return maxList

obj = Solution()
print(obj.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))