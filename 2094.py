from collections import Counter

class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        count = Counter(digits)
        ans = []
        
        for i in range(100, 1000, 2):
            s = str(i)
            i_count = Counter([int(c) for c in s])
            
            if all(count[d] >= i_count[d] for d in i_count):
                ans.append(i)
                
        return ans

obj = Solution()
print(obj.findEvenNumbers([2,2,8,8,2]))