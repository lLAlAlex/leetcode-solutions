class Solution(object):
    def numberOfAlternatingGroups(self, colors, k):
        """
        :type colors: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        
        for i in range(k-1):
            colors.append(colors[i])
            
        left = 0
        right = 1
            
        while right < len(colors):
            if colors[right] == colors[right - 1]:
                left = right
                right += 1
                continue
            
            right += 1
            
            if right - left < k:
                continue
            
            count += 1
            left += 1
        
        return count

obj = Solution()
print(obj.numberOfAlternatingGroups([0,1,0,1,0], 3))