class Solution(object):
    def removeDuplicates(self, nums):
        unique_nums = sorted(list(set(nums)))
        
        nums[:len(unique_nums)] = unique_nums
        
        return len(unique_nums)
        
obj = Solution()
print(obj.removeDuplicates([-1,0,0,0,0,3,3]))