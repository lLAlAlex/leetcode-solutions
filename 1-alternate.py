class Solution:
    def twoSum(self, nums: list[int], target: int):
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums[i+1:]:
                return [i, nums[i+1:].index(complement) + (i + 1)]

obj = Solution()
# obj.twoSum([3, 4, 5, 6], 7)
print(obj.twoSum([3, 4, 5, 6], 11))
        
# Input: 
# nums = [3,4,5,6], target = 7

# Output: [0,1]