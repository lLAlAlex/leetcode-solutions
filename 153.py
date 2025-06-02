class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        mid = 0
        
        ans = nums[0]
        
        while left <= right:
            if nums[left] < nums[right] :
                ans = min(ans, nums[left])
                break
            
            mid = (left + right) // 2
            
            ans = min(ans, nums[mid])
            
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        
        return ans

obj = Solution()
print(obj.findMin([3,4,5,6,1,2]))