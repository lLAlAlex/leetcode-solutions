class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sorted_arr = sorted(nums)
        
        for i in range(len(nums)):
            sorted_arr.insert(0, sorted_arr.pop())
            
            if sorted_arr == nums:
                return True
            
        return False
            
obj = Solution()
print(obj.check([3,4,5,1,2]))