from collections import Counter

class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        count = Counter(words)
        maxLen = 0
        used = False
        
        print(count)
        
        for word in count:
            reverse = word[::-1]
            if word == reverse:
                pairs = count[word] // 2
                maxLen += pairs * 4
                count[word] -= pairs * 2
                if not used and count[word] > 0:
                    maxLen += 2
                    used = True
            else:
                if reverse in count:
                    pairs = min(count[word], count[reverse])
                    maxLen += pairs * 4
                    count[word] -= pairs
                    count[reverse] -= pairs
            
        return maxLen

obj = Solution()
print(obj.longestPalindrome(["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]))