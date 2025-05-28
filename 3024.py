class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if (nums[0] >= nums[1] + nums[2]) or (nums[1] >= nums[0] + nums[2]) or (nums[2] >= nums[0] + nums[1]):
            return "none"
        
        nums = set(nums)
        
        if len(nums) == 1 : return "equilateral"
        
        return "isosceles" if len(nums) == 2 else "scalene"

obj = Solution()
print(obj.triangleType([5,3,8]))