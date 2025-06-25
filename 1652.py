class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(code)
        
        if k == 0:
            return [0] * n
        
        ans = []
        
        if k > 0:
            left = 1
            right = k
        else:
            left = n - abs(k)
            right = n - 1
            
        curr = sum(code[left:right+1])
        
        for _ in range(n):
            ans.append(curr)
            curr -= code[left]
            left = (left + 1) % n
            right = (right + 1) % n
            curr += code[right]
        
        return ans

obj = Solution()
print(obj.decrypt([5,2,2,3,1], 3))