class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        inc = []
        dec = []
        flag = False
        
        curr_inc = []
        curr_dec = []
        
        for i in range(len(nums)):
            curr_inc.append(nums[i])
            curr_dec.append(nums[i])
            
            if not flag:
                while curr_inc:
                    inc.append(curr_inc.pop())
                while curr_dec:
                    dec.append(curr_dec.pop())
                continue
            
            if nums[i+1] > nums[i]:
                flag = 1
                continue
            elif nums[i+1] < nums[i]:
                flag = 1
                continue

            flag = 0

obj = Solution()
print(obj.longestMonotonicSubarray([1,4,3,3,2]))