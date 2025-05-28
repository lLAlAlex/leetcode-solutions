from collections import defaultdict

class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        left = 0
        maxLen = 0
        temp = defaultdict(int)
        
        for right in range(len(fruits)):
            temp[fruits[right]] += 1
            
            while len(temp) > 2:
                temp[fruits[left]] -= 1
                if temp[fruits[left]] == 0:
                    del temp[fruits[left]]
                left += 1
            
            maxLen = max(maxLen, right - left + 1)
        
        return maxLen
    
obj = Solution()
print(obj.totalFruit([3,3,3,1,2,1,1,2,3,3,4]))