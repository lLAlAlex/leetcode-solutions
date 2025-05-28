class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        stack = [""]
        
        while stack:
            curr = stack.pop()
            
            if len(curr) == len(nums[0]):
                if curr not in nums:
                    return curr
                continue
            
            for char in ["0", "1"]:
                if len(curr) != len(nums[0]):
                    stack.append(curr + char)

obj = Solution()
print(obj.findDifferentBinaryString(["111","011","001"]))