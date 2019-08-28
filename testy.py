import sys; sys.stdin = open('data/(1247)input.txt', 'r')

from queue import Queue

def BFS(s, G):

    D[s] = 0
    Q = Queue()
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        for v, w in G[u]:
            if D[v] > D[u] + w:
                D[v] = D[u] + w
                P[v] = u
                Q.put(v)

TC = int(input())
for tc in range(10):

    n = int(input())
    data = list(map(int, input().split()))

    arr = []
    j = 1
    for i in range(0, len(data) - 1, 2):
        arr.append([j, data[i], data[i + 1]])
        j += 1

    arr[1][1:3], arr[-1][1:3] = arr[-1][1:3], arr[1][1:3]

    G = [[] for _ in range(n + 3)]
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            w = abs(arr[j][2] - arr[i][2]) + abs(arr[j][1] - arr[i][1])
            G[i + 1].append((j + 1, w))
            G[j + 1].append((i + 1, w))

    print(G)
    D = [0xfffff] * (n + 3)
    P = [i for i in range(n + 3)]

    BFS(1, G)
    #
    # print(D[1:])
    # print(P[1:])