import sys; sys.stdin = open('data/(5178)input.txt', 'r')

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
