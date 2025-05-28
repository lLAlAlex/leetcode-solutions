from collections import defaultdict

class Solution(object):
    def lengthAfterTransformations(self, s, t):
        """
        :type s: str
        :type t: int
        :rtype: int
        """
        arr = defaultdict(int)
        
        for c in s:
            arr[c] += 1
            
        for _ in range(t):
            temp = defaultdict(int)
            
            for c in arr:
                if c == 'z':
                    temp['a'] += arr[c]
                    temp['b'] += arr[c]
                else:
                    after = chr(ord(c) + 1)
                    temp[after] += arr[c]
            
            arr = temp
                 
        return sum(arr.values()) % (10**9 + 7)

obj = Solution()
print(obj.lengthAfterTransformations("jqktcurgdvlibczdsvnsg", 7517))