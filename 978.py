class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr) == 1:
            return len(arr)
        
        maxLen = 1
        windowLen = 1
        sign = ''
        
        for right in range(len(arr) - 1):
            if arr[right] == arr[right + 1]:
                windowLen = 1
                sign = ''
            else:
                curr = '>' if arr[right] > arr[right + 1] else '<'
                if sign == '' or sign != curr:
                    windowLen += 1
                else:
                    windowLen = 2
                sign = curr
            
            maxLen = max(maxLen, windowLen)
            
        return maxLen

obj = Solution()
print(obj.maxTurbulenceSize([8,8,9,10,6,8,2,4,2,2,10,6,6,10,10,2,3,5,1,2,10,4,2,0,9,4,9,3,0,6,3,2,3,10,10,6,4,6,4,4,2,5,1,4,1,1,9,8,9,5,3,5,5,4,5,5,6,5,3,3,7,2,0,10,9,7,7,3,5,1,0,9,6,3,1,3,4,4,3,6,3,2,1,4,10,2,3,4,4,3,6,7,6,2,1,7,0,6,8,10]))