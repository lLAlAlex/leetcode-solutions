class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        count = 0
        temp1 = []
        temp2 = []
        
        for num in range(low, high + 1):
            if len(str(num)) % 2 == 1:
                continue
            
            numStr = str(num)
            
            half = int(len(numStr) / 2)
            
            left = numStr[0:half]
            right = numStr[half:len(numStr)]
            
            for i in left:
                temp1.append(int(i))
                
            for i in right:
                temp2.append(int(i))
                
            if sum(temp1) == sum(temp2):
                count += 1

            temp1 = []
            temp2 = []
                
        return count
            
obj = Solution()
print(obj.countSymmetricIntegers(100, 1782))