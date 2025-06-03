class Solution(object):
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        """
        :type status: List[int]
        :type candies: List[int]
        :type keys: List[List[int]]
        :type containedBoxes: List[List[int]]
        :type initialBoxes: List[int]
        :rtype: int
        """
        seen = set()
        candidate = set()
        
        def dfs(box):
            # base case
            if box in seen:
                return 0
            
            # mark unavailable boxes
            if status[box] == 0:
                candidate.add(box)
                return 0
            
            seen.add(box)
            ans = candies[box]
            
            # check all possible boxes
            for boxes in containedBoxes[box]:
                ans += dfs(boxes)
            
            # calculate unavailable boxes that have keys
            for key in keys[box]:
                status[key] = 1
                if key in candidate:
                    ans += dfs(key)
            
            return ans
        
        return sum([dfs(box) for box in initialBoxes])

obj = Solution()
print(obj.maxCandies([1,0,1,0], [7,5,4,100], [[],[],[1],[]], [[1,2],[3],[],[]], [0]))