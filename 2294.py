class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        ans = 1
        left = nums[0]
        
        for num in nums:
            if num - left > k:
                ans += 1
                left = num
        
        return ans

obj = Solution()
print(obj.partitionArray([1,2,3,5,6], 2))