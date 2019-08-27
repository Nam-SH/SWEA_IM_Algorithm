import sys; sys.stdin = open('data/(5102)input.txt', 'r')
from collections import deque

def find(arr, s, g):
    global res
    check = [False for _ in range(v + 1)]
    q = deque()
    q.append(s)
    check[s] = True

    while q:
        s = q.popleft()
        for k in arr[s]:
            if not check[k] and arr[k]:
                check[k] = True
                q.append(k)
            if k == g:
                return

T = int(input())
for tc in range(T):
    v, e = map(int, input().split())

    arr = [[] for _ in range(v + 1)]
    res = 0


    for _ in range(e):
        i, j = map(int, input().split())
        arr[i].append(j)
        arr[j].append(i)
    s, g = map(int, input().split())
    find(arr, s, g)
    print()
    print()
