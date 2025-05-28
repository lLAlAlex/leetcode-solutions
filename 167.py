from collections import defaultdict

class Solution:
    def twoSum(self, numbers, target):
        var = defaultdict(int)
        
        for i in range(len(numbers)):
            temp = target - numbers[i]
            
            if var[temp]:
                return [var[temp], i + 1]
            var[numbers[i]] = i + 1
        return []
            
obj = Solution()
print(obj.twoSum([2, 3, 4], 6))