class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        ans = []
        right = 0
        
        for i in range(len(nums)):
            if nums[i] == key:
                left = max(right, i - k)
                right = min(len(nums) - 1, i + k) + 1
                
                for idx in range(left, right):
                    if idx not in ans:
                        ans.append(idx)
        
        return ans

obj = Solution()
print(obj.findKDistantIndices([3,4,9,1,3,9,5], 9, 1))