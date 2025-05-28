from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = defaultdict(list)
        
        for str in strs:
            key = ''.join(sorted(str))
            anagrams[key].append(str)
    
        return list(anagrams.values())
        
obj = Solution()
obj.groupAnagrams(["eat","tea","tan","ate","nat","bat"])