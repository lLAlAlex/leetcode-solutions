class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        
        max = 0
        count = 1
        nums.sort()
        
        for i in range(len(nums) - 1):
            if nums[i+1] - nums[i] == 1:
                count += 1
            elif nums[i+1] - nums[i] == 0:
                continue
            else:
                if max < count:
                    max = count
                count = 1
        
        if max < count:
            max = count
            
        return max

obj = Solution()
print(obj.longestConsecutive([]))