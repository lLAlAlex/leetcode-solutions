from collections import defaultdict

class Solution(object):
    def threeSum(self, nums):
        nums = list(nums)
        nums.sort()
        var = defaultdict(int)
        for num in nums:
            var[num] += 1
            
        res = []
        
        for i in range(len(nums)):
            var[nums[i]] -= 1
            if i and nums[i] == nums[i-1]:
                continue
            
            for j in range(i + 1, len(nums)):
                var[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j-1]:
                    continue
                target = -(nums[i] + nums[j])
                
                if var[target] > 0:
                    res.append((nums[i], nums[j], target))
                
            for j in range(i+1, len(nums)):
                var[nums[j]] += 1
        
        return res

obj = Solution()
print(obj.threeSum([0,0,0]))