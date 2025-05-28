from collections import defaultdict

class Solution(object):
    # def checkIfExist(self, arr):
    #     for i in range(len(arr)):
    #         for j in range(len(arr)):
    #             if i!=j and arr[i] == arr[j] * 2:
    #                 return True
    #     return False
    
    def checkIfExist(self, arr):
        seen = set()
        
        for i in range(len(arr)):
            if arr[i] * 2 in seen or (arr[i] % 2 == 0 and arr[i] // 2 in seen):
                return True
            seen.add(arr[i])
        return False
        
obj = Solution()
print(obj.checkIfExist([3,1,7,11]))