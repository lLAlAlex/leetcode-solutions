class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # res = []
        
        # def generateSubarray(arr, start, end):
        #     if end == len(arr):
        #         return
            
        #     elif start > end:
        #         return generateSubarray(arr, 0, end + 1)
            
        #     else:
        #         res.append(arr[start:end+1])
        #         return generateSubarray(arr, start + 1, end)
        
        # generateSubarray(arr, 0, 0)
        
        # for i in range(len(res)):
        #     temp = sum(res[i])
        #     if temp % 2 != 0:
        #         odd_count += 1
        count = sum_temp = 0
        odd_prefix = 0
        even_prefix = 1
        MOD = 10**9 + 7
        
        for num in arr:
            sum_temp += num
            
            if sum_temp % 2 == 0:
                count += odd_prefix
                even_prefix += 1
            else:
                count += even_prefix
                odd_prefix += 1
            
            count %= MOD
            
        return count
        
obj = Solution()
print(obj.numOfSubarrays([1,3,5]))