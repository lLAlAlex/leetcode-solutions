from collections import defaultdict

class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        hashmap = defaultdict(list)
        
        for num in nums1:
            hashmap[num[0]] = num[1]
        
        for num in nums2:
            if hashmap[num[0]]:
                hashmap[num[0]] += num[1]
            else:
                hashmap[num[0]] = num[1]
        
        return sorted([[key, value] for key, value in hashmap.items()])

obj = Solution()
print(obj.mergeArrays([[1,2],[2,3],[4,5]], [[1,4],[3,2],[4,1]]))