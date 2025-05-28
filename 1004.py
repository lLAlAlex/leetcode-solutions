class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        maxLen = 0
        windowLen = 0
        zeros = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            windowLen = right - left + 1
            maxLen = max(maxLen, windowLen)
        
        return maxLen

obj = Solution()
print(obj.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))