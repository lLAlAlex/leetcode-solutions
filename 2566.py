class Solution(object):
    def minMaxDifference(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = [int(digit) for digit in str(num)]
        firstNonNine, firstNonZero = 9, 0
        minNum = []
        maxNum = []
        
        for n in num:
            if n != 9:
                firstNonNine = n
                break
        
        for n in num:
            if n != 0:
                firstNonZero = n
                break
        
        for i in range(len(num)):
            if num[i] == firstNonNine:
                maxNum.append(9)
            else:
                maxNum.append(num[i])
                
            if num[i] == firstNonZero:
                minNum.append(0)
            else:
                minNum.append(num[i])
        
        return int("".join(map(str, maxNum))) - int("".join(map(str, minNum)))
    
obj = Solution()
print(obj.minMaxDifference(90))