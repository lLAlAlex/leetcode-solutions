class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        """
        matrix = list(range(26))
        ans = []
        
        def find(x):
            if matrix[x] != x:
                matrix[x] = find(matrix[x])
            return matrix[x]
            
        def union(x, y):
            px, py = find(x), find(y)
            
            if px < py:
                matrix[py] = px
            else:
                matrix[px] = py
        
        for a, b in zip(s1, s2):
            x1 = ord(a) - ord('a')
            x2 = ord(b) - ord('a')
            union(x1, x2)

        for c in baseStr:
            smallest = chr(find(ord(c) - ord('a')) + ord('a'))
            ans.append(smallest)
        
        return ''.join(ans)

obj = Solution()
print(obj.smallestEquivalentString("parker", "morris", "parser"))