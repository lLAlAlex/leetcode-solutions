inp = input()
ans = []

low = ""
up = ""
num = ""
odd = ""
even = ""

for i in range(len(inp)):
    if ord(inp[i]) > 96:
        low += inp[i]
    elif ord(inp[i]) > 64:
        up += inp[i]
    else:
        num += inp[i]

for n in num:
    if int(n) % 2 == 0:
        even += n
    else:
        odd += n

res = ''.join(sorted(low)) + ''.join(sorted(up)) + ''.join(sorted(odd)) + ''.join(sorted(even))
print(res)