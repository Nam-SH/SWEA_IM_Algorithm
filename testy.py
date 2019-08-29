import sys; sys.stdin = open('data/(1238)input.txt', 'r')
from collections import deque

def find(s):
    q = deque()
    q.append(s)
    V[s] = True

    while q:
        u = q.popleft()
        for w in G[u]:
            if not V[w]:
                V[w] = True
                q.append(w)
                D[w] = D[u] + 1
    return

for tc in range(10):
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    G = [[] for _ in range(101)]
    D = [0] * 101

    V = [False] * 101
    for i in range(0, N, 2):
        G[arr[i]].append(arr[i + 1])
    find(S)

    for i in range(100, -1, -1):
        if D[i] == max(D):
            print('#{} {}'.format(tc + 1, i))
            break



# def check(start):
#     max_D = 0
#     Q.append(start)
#     visit[start] = True
#     while Q:
#         v = Q.pop(0)
#         for w in G[v]:
#             if visit[w]: continue
#             visit[w] = True
#             Q.append(w)
#             D[w] = D[v] + 1
#             max_D = max(D[w], max_D)
#     return max_D
#
#
# for t in range(1, 11):
#     N, S = map(int, input().split())
#     arr = list(map(int, input().split()))
#     G = [[] for _ in range(101)]
#     D = [0] * 101
#     Q = []
#     visit = [False] * 101
#     for i in range(N // 2):
#         G[arr[i * 2]].append(arr[i * 2 + 1])
#     print(G)
#     max_D = check(S)
#     for i in range(100, 0, -1):
#         if D[i] == max_D:
#             print('#{} {}'.format(t, i))
#             break