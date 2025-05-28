from itertools import combinations

class Solution(object):
    def partition(self, num):
        partitions = []
        
        for x in range(1, len(num)):
            for i in combinations(range(1, len(num)), x):
                parts = []
                last_idx = 0
                
                for idx in i:
                    parts.append(num[last_idx:idx])
                    last_idx = idx
                
                parts.append(num[last_idx:])
                partitions.append(parts)
                
        return partitions
    
    def punishmentNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        matches = []
        
        for i in range(1, n+1):
            res = i * i
            
            if res == i:
                matches.append(res)
                continue
            
            partitions = self.partition(str(res))
            
            for parts in partitions:
               if sum(map(int, parts)) == i:
                   matches.append(res)
                   break 
            
        return sum(matches)

obj = Solution()
print(obj.punishmentNumber(10))