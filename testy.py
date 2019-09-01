import sys; sys.stdin = open('data/(5178)input.txt', 'r')

<<<<<<< HEAD
def find(n):

    l_n = n * 2
    r_n = n * 2 + 1
    if r_n > N and l_n > N: return
    find(l_n)
    find(r_n)
    arr[n] = arr[r_n] + arr[l_n]


for tc in range(int(input())):
    N, M, L = map(int, input().split())
    arr = [0]*(N + 1) + [0]

    for _ in range(M):
        idx, val = map(int, input().split())
        arr[idx] = val
    find(1)
    print('#{} {}'.format(tc + 1, arr[L]))
=======
def bfs(s):
    global res
    q.append(s)
    visit[s] = True

    while q:
        s = q.popleft()
        for k in arr[s]:
            if arr[k] and not visit[k]:
                q.append(k)
                visit[k] = True
                num[k] = num[s] +1
                if k == g:
                    res = num[k]
                    return

for tc in range(int(input())):
    v, e = map(int, input().split())
    arr = [[0] * (v+1) for _ in range(v+1)]
    visit = [False] * (v+1)
    num = [0] * (v+1)
    res = 0
    for i in range(e):
        i, j = map(int, input().split())
        arr[i].append(j)
        arr[j].append(i)

    s, g = map(int, input().split())
    q = deque()
    bfs(s)

    print('#{} {}'.format(tc + 1, res))
>>>>>>> 74889f2... 20190827 |
