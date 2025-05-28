class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        currDiff = None
        currLength = 1
        
        for right in range(1, len(nums)):
            diff = nums[right] - nums[right-1]
            
            if currDiff is None or currDiff != diff:
                currDiff = diff
                currLength = 2
            else:
                currLength += 1
                
            if currLength >= 3:
                count += currLength - 2
        
        return count

obj = Solution()
print(obj.numberOfArithmeticSlices([1,2,3,4]))