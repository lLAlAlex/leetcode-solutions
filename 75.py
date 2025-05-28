class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeros = []
        ones = []
        twos = []
        
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros.append(0)
            elif nums[i] == 1:
                ones.append(1)
            elif nums[i] == 2:
                twos.append(2)
        
        nums[:] = zeros + ones + twos
        
obj = Solution()
obj.sortColors([2, 0, 2, 1, 1, 0])