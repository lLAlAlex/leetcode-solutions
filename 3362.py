class Solution(object):
    def maxRemoval(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        ans = len(queries)
        
        for query in queries:
            flag = False
            
            if nums[query[0]] == 0 or nums[query[1]] == 0:
                continue
            
            print(query)
            
            if nums[query[0]] > 0:
                nums[query[0]] -= 1
                flag = True
            
            if nums[query[1]] > 0:
                nums[query[1]] -= 1
                flag = True
                
            if flag:
                ans -= 1
            
            if all(v == 0 for v in nums):
                return ans
        
        return -1

obj = Solution()
print(obj.maxRemoval([1,3], [[1,1],[0,1],[1,1],[0,1]]))