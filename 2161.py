class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        left = []
        pivot_arr = []
        right = []
        
        for num in nums:
            if num < pivot:
                left.append(num)
            elif num == pivot:
                pivot_arr.append(num)
            else:
                right.append(num)
        
        return left + pivot_arr + right

obj = Solution()
print(obj.pivotArray([9,12,5,10,14,3,10], 10))