import math

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0
        
        left = 0
        count = 0
        curr = 1
        
        for right in range(len(nums)):
            curr *= nums[right]

            while curr >= k:
                curr /= nums[left]
                left += 1
                
            count += right - left + 1
                
        return count

obj = Solution()
print(obj.numSubarrayProductLessThanK([10,5,2,6], 100))