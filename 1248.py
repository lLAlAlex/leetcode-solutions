class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        oddCount = 0
        left = 0
        res = 0
        
        for right in range(len(nums)):
            if nums[right] % 2 != 0 and oddCount == k:
                left += 1
                oddCount -= 1
                
            if nums[right] % 2 != 0:
                oddCount += 1
                
            if oddCount == k:
                for i in range(left, len(nums[:right + 1])):
                    print(nums[i:right + 1])
                    res += 1
                    
                    if nums[i] % 2 != 0:
                        break
                        
        return res

obj = Solution()
print(obj.numberOfSubarrays([1,1,2,1,1], 3))