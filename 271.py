class Solution:
    def encode(self, strs):
        return "".join(f"{len(s)}:{s}" for s in strs)

    def decode(self, s):
        if not s:
            return []
    
        res = []
        i = 0
        
        while i < len(s):
            j = s.find(":", i)
            length = int(s[i:j])
            
            res.append(s[j+1 : j+1+length])
            
            i = length + j + 1
            
        return res

obj = Solution()
print(obj.decode(obj.encode(["asd", "tes"])))