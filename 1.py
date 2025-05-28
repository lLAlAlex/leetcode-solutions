class Solution(object):
    import numpy as np
    
    def __init__(self):
        self.data = {}
        self.data["index"] = []
        self.data["value"] = []
    
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            complement = target - nums[i]
            print(f"Complement: {complement}")
            print(f"Index: {nums.index(complement)}")
            
            if complement in nums and nums.index(complement) != i:
                # print(f"Index: {i}")
                self.data["index"].append(i)
                self.data["value"].append(nums[i])
                print(self.data["index"])
        
        return self.data["index"]

def main():
    obj = Solution()
    obj.twoSum([3, 3], 6)
    
if __name__ == '__main__':
    main()