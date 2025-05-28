class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        
        if "B" * k in blocks:
            return 0
        
        possibilities = len(blocks) - (k-1)
        substrs = []
        counts = []
        
        for i in range(possibilities):
            substrs.append(blocks[i:i+k])
            
        for s in substrs:
            counts.append(s.count("W"))
        
        return min(counts)

obj = Solution()
print(obj.minimumRecolors("WBBWWBBWBW", 7))