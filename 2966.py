class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        
        for i in range(2, len(nums), 3):
            if nums[i] - nums[i - 2] > k:
                return []
            ans.append([nums[i-2], nums[i-1], nums[i]])
        
        return ans
    
obj = Solution()
print(obj.divideArray([2,4,2,2,5,2], 2))