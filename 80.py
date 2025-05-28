class Solution(object):
    def removeDuplicates(self, nums):
        stack = []
        
        for num in nums:
            if stack.count(num) < 2:
                stack.append(num)
                
        nums[:len(stack)] = stack
        
        return len(stack)
    
obj = Solution()
print(obj.removeDuplicates([0,0,1,1,1,1,2,3,3]))