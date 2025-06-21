from collections import defaultdict

class Solution(object):
    def minimumDeletions(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        arr = defaultdict(int)
        
        for c in word:
            arr[c] += 1
        
        res = len(word)
        
        for i in arr.values():
            temp = 0
            for j in arr.values():
                if j < i:
                    temp += j
                elif j > i + k:
                    temp += j - (i + k)
            
            res = min(res, temp)
        
        return res

obj = Solution()
print(obj.minimumDeletions("aabcaba", 0))