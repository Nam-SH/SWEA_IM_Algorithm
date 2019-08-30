import sys; sys.stdin = open('data/(5110)input.txt', 'r')
from collections import deque

for tc in range(int(input())):
    N, M = map(int, input().split())
    q = deque()
    q.extend(input().split())

    for i in range(M - 1):
        data = input().split()
        if int(max(q)) < int(data[0]):
            q.extend(data)

        elif int(min(q)) > int(data[0]):
            q.extendleft(data)

        else:
            for j in range(len(q)):
                if int(q[j]) > int(data[0]):
                    for k in range(len(data)):
                        q.insert(j, data[k])
                        j += 1
                    break

    print('#' + str(tc + 1), end = ' ')
    for i in range(1, 11): print(q[-i], end=' ')
    print()