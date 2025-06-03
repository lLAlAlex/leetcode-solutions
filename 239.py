from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        maxList = []
        
        que = deque()
        
        l = r = 0
        
        

obj = Solution()
print(obj.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))