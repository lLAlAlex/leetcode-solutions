#!/bin/python3
from collections import Counter

if __name__ == '__main__':
    s = input()

    count = Counter(s)
    curr = 0
    
    count = dict(sorted(count.items(), key=lambda x: x[0]))
    count = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))
    
    for key, value in count.items():
        print(key, value)
        curr += 1
        
        if curr == 3:
            break