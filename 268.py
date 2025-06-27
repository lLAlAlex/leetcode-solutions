class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = sum(nums)
        expected = n * (n + 1) // 2
        
        return abs(expected - total)

obj = Solution()
print(obj.missingNumber([3, 0 ,1]))