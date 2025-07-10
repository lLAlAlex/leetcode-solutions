def merge_the_tools(string, k):
    temp = []
    ans = []
    
    for i in range(len(string)):
        if string[i] not in temp:
            temp.append(string[i])
        
        if (i + 1) % k == 0:
            ans.append("".join(temp))
            temp = []
    
    for x in ans:
        print(x)

merge_the_tools("AABCAAADA", 3)