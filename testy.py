import sys; sys.stdin = open('data/(1225)input.txt', 'r')
from collections import deque

for _ in range(10):
    q = deque()
    tc = input()
    arr = input().split()
    for i in arr:
        q.append(int(i))

    j = 1
    while 0 not in q:
        q[0] -= j
        q.append(q.popleft())

        if q[-1] <= 0:
            q[-1] = 0
            break
        j += 1
        if j > 5: j = 1
    print('#' + tc, *q)