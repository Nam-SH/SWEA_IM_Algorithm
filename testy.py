import sys; sys.stdin = open('data/(1227)input.txt', 'r')
from collections import deque

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visit[i][j] = 1
    while q:
        i, j = q.popleft()
        for dy, dx in (0, 1), (0, -1), (1, 0), (-1, 0):
            ty = i + dy
            tx = j + dx
            if arr[ty][tx] == '3':
                return 1
            elif arr[ty][tx] == '0' and (ty, tx) and not visit[ty][tx]:
                visit[ty][tx] = 1
                q.append((ty, tx))
    return 0

for _ in range(10):
    tc = int(input())
    arr = [input() for _ in range(100)]
    visit = [[0] * 100 for _ in range(100)]
    print('#{} {}'.format(tc, bfs(2, 1)))
