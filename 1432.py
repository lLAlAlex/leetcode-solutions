class Solution(object):
    def maxDiff(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = [int(digit) for digit in str(num)]
        firstMax = num[0]
        firstMin = num[0]
        maxArr = []
        minArr = []
        
        for n in num:
            if n != 9:
                firstMax = n
                break
        
        for n in num:
            if n > 1:
                firstMin = n
                break
        
        # print(firstMax)
        # print(firstMin)
        
        for i in range(len(num)):
            if num[i] == firstMax:
                maxArr.append(9)
            else:
                maxArr.append(num[i])
        
        for i in range(len(num)):
            if num[i] == firstMin and firstMin != num[0]:
                minArr.append(0)
            elif num[i] == firstMin:
                minArr.append(1)
            else:
                minArr.append(num[i])
        
        # print(maxArr)
        # print(minArr)
        
        return int("".join(map(str, maxArr))) - int("".join(map(str, minArr)))

obj = Solution()
print(obj.maxDiff(555))