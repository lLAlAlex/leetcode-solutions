class Solution(object):
    def lenLongestFibSubseq(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        maxLen = 0
        res = set(arr)
        
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                prev = arr[j]
                curr = arr[i] + prev
                currLen = 2
                
                while curr in res:
                    prev, curr = curr, curr + prev
                    currLen += 1
                    
                    if currLen > maxLen:
                        maxLen = currLen
        
        return maxLen if maxLen > 2 else 0

obj = Solution()
print(obj.lenLongestFibSubseq([1,2,3,4,5,6,7,8]))