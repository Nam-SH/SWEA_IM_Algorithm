import sys; sys.stdin = open('data/(5099)input.txt', 'r')
from collections import deque

for tc in range(int(input())):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    q = deque()

    for i in range(N): q.append([arr[i], i + 1])

    j = 0
    while len(q) != 1:
        q[0][0] //= 2

        if q[0][0] != 0: q.append(q.popleft())
        else:
            if N + j < M:
                q.popleft()
                q.append([arr[N + j], N + j + 1])
                j += 1
            else: q.popleft()

    print('#{} {}'.format(tc + 1, q[0][1]))