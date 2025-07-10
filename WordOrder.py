from collections import defaultdict

num = int(input())
arr = []

for i in range(num):
    s = input()
    arr.append(s)

d = defaultdict(int)
    
for s in arr:
    d[s] += 1

print(len(d))
for x in d.values():
    print(x, end=" ")