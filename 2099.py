class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        arr = [[i, nums[i]] for i in range(len(nums))]
        arr.sort(key=lambda x: -x[1])
        arr = sorted(arr[:k])
        ans = [e for _, e in arr]
        return ans

obj = Solution()
print(obj.maxSubsequence([2,1,3,3], 2))