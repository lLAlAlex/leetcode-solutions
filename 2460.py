class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
            else:
                continue
        
        for num in nums:
            if num == 0:
                nums.remove(num)
                nums.append(0)
            
        return nums

obj = Solution()
print(obj.applyOperations([1,2,2,1,1,0]))