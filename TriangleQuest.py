inp = int(input())

for i in range(1, inp):
    count = 0
    temp = []
    for j in range(1, inp):
        if count == i:
            break
        print(i, end="")
        count += 1
    print("")