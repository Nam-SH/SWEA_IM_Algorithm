import sys; sys.stdin = open('data/(5177)input.txt', 'r')

import heapq

for tc in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))

    heap = []
    for i in arr:
        heapq.heappush(heap, i)
    res = 0
    while N - 1 >= 1:
        N //= 2
        res += heap[N - 1]
    print('#{} {}'.format(tc + 1, res))