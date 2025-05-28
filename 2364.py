from collections import defaultdict

class Solution(object):
    def countBadPairs(self, nums):
        good_pairs = 0
        hash_map = defaultdict(int)
        
        total_pairs = len(nums) * (len(nums) - 1) // 2
        # for i in range(len(nums)):
        #     for j in range(i+1):
        #         if j-i != nums[j]-nums[i]:
        #             count += 1
        for i, num in enumerate(nums):
            key = num - i
            good_pairs += hash_map[key]
            hash_map[key] += 1
        
        return total_pairs - good_pairs

obj = Solution()
print(obj.countBadPairs([4, 1, 3, 3]))