class Solution(object):
    def minSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # temp1 = []
        # temp2 = []
        # count1 = 0
        # count2 = 0
        
        # for i in range(len(nums1)):
        #     temp1.append(nums1[i])
        #     if nums1[i] == 0:
        #         count1 += 1
        #         temp1.append(1)
        
        # for i in range(len(nums2)):
        #     temp2.append(nums2[i])
        #     if nums2[i] == 0:
        #         count2 += 1
        #         temp2.append(1)
        
        # if sum(temp2) == sum(temp1):
        #     return sum(temp2)
        # elif sum(temp2) > sum(temp1):
        #     if count1 == 0:
        #         return -1
        #     target = sum(temp2) - sum(temp1) + count1
        #     temp1 = nums1
            
        #     for i in range(len(temp1)):
        #         if temp1[i] == 0:
        #             temp1[i] = target / count1
        # else:
        #     if count2 == 0:
        #         return -1
        #     target = sum(temp1) - sum(temp2) + count2
        #     temp2 = nums2
            
        #     for i in range(len(temp2)):
        #         if temp2[i] == 0:
        #             temp2[i] = target / count2
        
        # return int(round(sum(temp2))) if int(round(sum(temp2))) == int(round(sum(temp1))) else -1
        zeros1 = nums1.count(0)
        zeros2 = nums2.count(0)
        
        temp1 = nums1
        temp2 = nums2
        
        for i in range(len(temp1)):
            if temp1[i] == 0:
                temp1[i] = 1
        
        for i in range(len(temp2)):
            if temp2[i] == 0:
                temp2[i] = 1
                
        sum1 = sum(temp1)
        sum2 = sum(temp2)
        
        if sum1 > sum2 and zeros2 == 0 or sum2 > sum1 and zeros1 == 0:
            return -1
        
        if sum1 == sum2:
            return sum1
        
        return sum2 if sum1 < sum2 else sum1

obj = Solution()
print(obj.minSum([3,0,20,9,20,0,20,25,26,9,0,12,6,11,0,6], [0,3,8,13,27,0,0,0,29,27,0,11,23,0,19,19,0]))