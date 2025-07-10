def solve(s):
    flag = False
    ans = s[0].upper()
    
    for i in range(1, len(s)):
        if s[i] == " ":
            flag = True
            ans += s[i]
            continue
        
        if flag:
            ans += s[i].upper()
            flag = False
        else:
            ans += s[i]
    
    return ans

print(solve("hello world"))