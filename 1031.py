class Solution(object):
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        """
        :type nums: List[int]
        :type firstLen: int
        :type secondLen: int
        :rtype: int
        """
        def helper(L, R):
            firstWindowSum = sum(nums[:L])
            firstMax = firstWindowSum
            secondWindowSum = sum(nums[L:L+R])
            totalMax = firstMax + secondWindowSum
            
            for i in range(L + R, len(nums)):
                # print(f"First Sum: {firstWindowSum}")
                firstWindowSum = firstWindowSum + nums[i - R] - nums[i - L - R]
                firstMax = max(firstMax, firstWindowSum)
                
                # print(f"Second Sum: {secondWindowSum}")
                secondWindowSum = secondWindowSum + nums[i] - nums[i - R]
                totalMax = max(totalMax, firstMax + secondWindowSum)
                
            return totalMax
        
        return max(helper(firstLen, secondLen), helper(secondLen, firstLen))

obj = Solution()
print(obj.maxSumTwoNoOverlap([2,1,5,6,0,9,5,0,3,8], 4, 3))