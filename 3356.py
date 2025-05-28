class Solution(object):
    def minZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        count = 0
        
        for query in queries:
            l = query[0]
            r = query[1]
            val = query[2]
            
            for num in nums[l:r+1]:
                if num != 0:
                    num -= val
            
            print(nums)
        
        return count
            

obj = Solution()
print(obj.minZeroArray([2,0,2], [[0,2,1],[0,2,1],[1,1,3]]))