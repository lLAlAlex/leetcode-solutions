import heapq

class Solution(object):
    count = 0
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)
        
        while nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums, min(x, y) * 2 + max(x, y))
            self.count += 1
            
        return self.count
    
obj = Solution()
print(obj.minOperations([1,1,2,4,9], 20))