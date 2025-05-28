from collections import defaultdict

class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashMap = defaultdict(list)
        maxList = []
        
        for i in range(len(nums)):
            sumNum = 0
            
            for j in str(nums[i]):
                sumNum += int(j)
            
            if not hashMap[sumNum] or len(hashMap[sumNum]) < 2:
                hashMap[sumNum].append(nums[i])
            else:
                if hashMap[sumNum][0] < nums[i]:
                    if len(hashMap[sumNum]) > 1:
                        hashMap[sumNum][0] = nums[i]
                    else:
                        hashMap[sumNum].append(nums[i])
                        
            hashMap[sumNum].sort()
            
        for i in hashMap:
            if len(hashMap[i]) > 1:
                maxList.append(hashMap[i][0] + hashMap[i][1])
            
        if maxList:
            return max(maxList)
        return -1

obj = Solution()
print(obj.maximumSum([18,43,36,13,7]))