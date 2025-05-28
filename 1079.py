from collections import defaultdict

class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        res = set()
        flag = [False] * len(tiles)
        
        def generateSequence(tiles, current, flag):
            if len(tiles) == 1:
                return 1
            
            res.add(current)
            
            for i in range(len(tiles)):
                char = tiles[i]
                
                if not flag[i]:
                    flag[i] = True
                    generateSequence(tiles, current + char, flag)
                    flag[i] = False
        
        generateSequence(tiles, "", flag)
        
        if generateSequence(tiles, "", flag) == 1:
            return 1
        
        return len(res) - 1

obj = Solution()
print(obj.numTilePossibilities("AAB"))