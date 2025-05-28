class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        mid = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (high + low) // 2
            
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid
        
        return -1
        
obj = Solution()
print(obj.search([-1,0,2,4,6,8], 4))