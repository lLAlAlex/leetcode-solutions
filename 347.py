from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        res = [item[0] for item in Counter(nums).most_common(k)]
        # print(res)
        return res
        
obj = Solution()
obj.topKFrequent([1,2,2,3,3,3], 2)