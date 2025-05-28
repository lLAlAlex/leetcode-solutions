class Solution(object):
    def constructDistancedSequence(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        arr = [0] * (2 * n - 1)
        used = []
        
        def backtrack(index):
            if index == len(arr):
                return True
            
            if arr[index] != 0:
                return backtrack(index + 1)
            
            for num in range(n, 0, -1):
                if num in used:
                    continue
                
                if num == 1:
                    arr[index] = 1
                    used.append(1)
                    
                    if backtrack(index):
                        return True
                    
                    arr[index] = 0
                    used.remove(1)
                
                elif index + num < len(arr) and arr[index + num] == 0:
                    arr[index] = arr[index + num] = num
                    used.append(num)
                    
                    if backtrack(index + 1):
                        return True
                    
                    arr[index] = arr[index + num] = 0
                    used.remove(num)
            
            return False
        
        backtrack(0)
        
        return arr

obj = Solution()
print(obj.constructDistancedSequence(7))