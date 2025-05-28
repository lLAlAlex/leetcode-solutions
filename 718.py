class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        def checkSubarray(arr, subarr):
            n, m = len(arr), len(subarr)
            for i in range(n - m + 1):
                if arr[i:i + m] == subarr:
                    return True
            return False
        
        maxLen = 0
        left = 0
        
        for right in range(len(nums1)):
            maxLen += 1
            
            if checkSubarray(nums2, nums1[left:right+1]) == False:
                maxLen -= 1
                left += 1
              
        return maxLen

obj = Solution()
print(obj.findLength([1,2,3,2,1], [3,2,1,4,7]))