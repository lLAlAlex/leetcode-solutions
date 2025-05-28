class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        rows, cols = (m, n)
        map = [[0] * cols] * rows
        
        for wall in walls:
            print(f"Map: {wall}")
            print(f"Map Before: {map}")
            map[0][0] = 1
            print(f"Map After: {map}")
        # for guard in guards:
        #     print(guard)
        #     map[guard[0]][guard[1]] = "2"
    
obj = Solution()
obj.countUnguarded(4, 6, [[0,0],[1,1],[2,3]], [[0,1],[2,2],[1,4]])