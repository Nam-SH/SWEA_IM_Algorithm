import sys; sys.stdin = open('data/(5110)input.txt', 'r')
from collections import deque

for tc in range(int(input())):
    N, M = map(int, input().split())
    q = deque()
    q.extend(map(int, input().split()))

    for i in range(M - 1):
        data = deque()
        data.extend(map(int, input().split()))
        if max(q) < data[0]:
            q.extend(data)
        else:
            for j in range(len(q)):
                if q[j] > data[0]:
                    for k in range(len(data)):
                        q.insert(j, data[k])
                        j += 1
                    break

    print('#' + str(tc + 1), end = ' ')
    for i in range(1, 11): print(q[-i], end=' ')
    print()