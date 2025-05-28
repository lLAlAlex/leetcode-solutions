class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        currSum = 0
        minLen = float('inf')
        
        for right in range(len(nums)):
            currSum += nums[right]
            
            while currSum >= target:
                minLen = min(minLen, right - left + 1)
                currSum -= nums[left]
                left += 1
        
        return minLen if minLen != float('inf') else 0

obj = Solution()
print(obj.minSubArrayLen(7, [2,3,1,2,4,3]))