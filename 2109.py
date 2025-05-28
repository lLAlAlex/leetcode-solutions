class Solution(object):
    def addSpaces(self, s, spaces):
        str = []
        space_set = set(spaces)
        
        for i, char in enumerate(s):
            if i in space_set:
                str.append(" ")
            str.append(char)
            # s = s[:spaces[i]+i] + " " + s[spaces[i]+i:]
            
        return "".join(str)

obj = Solution()
print(obj.addSpaces("LeetcodeHelpsMeLearn", [8, 13, 15]))