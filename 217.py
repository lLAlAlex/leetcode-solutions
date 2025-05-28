class Solution:
    def validate(self, lst):
        seen = set()
        for num in lst:
            if num in seen:
                return True
            seen.add(num)
        return False
    
    def hasDuplicate(self, nums: list[int]) -> bool:
        return self.validate(nums)

# solution = Solution()
# solution.hasDuplicate([1, 2, 3])