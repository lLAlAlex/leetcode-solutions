inp = input()
res = []
curr = 0
left = 0

for right in range(len(inp)):
    if inp[left] != inp[right]:
        res.append((curr, int(inp[left])))
        while inp[left] != inp[right]:
            left += 1
            curr -= 1
            
    curr += 1

res.append((len(inp) - left, int(inp[left])))

for r in res:
    print(r, end=" ")