class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x = 16
        max_power = 3**x
        temp = 0
        
        while n < max_power:
            x -= 1
            max_power = 3**x
        
        while n > 0:
            max_power = 3**x
            if n >= max_power:
                n -= max_power
            if n >= max_power:
                return False
            
            x -= 1
        
        return True

obj = Solution()
print(obj.checkPowersOfThree(12))