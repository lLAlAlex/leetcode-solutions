class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        def convert(c):
            if c == 'I': return 1
            elif c == 'V': return 5
            elif c == 'X': return 10
            elif c == 'L': return 50
            elif c == 'C': return 100
            elif c == 'D': return 500
            elif c == 'M': return 1000
            return 0
        
        ans = 0
        prev_value = 0
        
        for c in reversed(s):
            curr_value = convert(c)
            if curr_value >= prev_value:
                ans += curr_value
            else:
                ans -= curr_value
            prev_value = curr_value
        
        return ans

obj = Solution()
print(obj.romanToInt("MCMXCIV"))