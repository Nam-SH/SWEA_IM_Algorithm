import sys; sys.stdin = open('data/(5177)input.txt', 'r')
from heapq import heapify


for tc in range(int(input())):
    N = int(input())
    heap = list(map(int, input().split()))
    heapify(heap)
    print(heap)
    heap = [0] + heap
    res = 0
    while N >= 1:
        N //= 2
        res += heap[N]
    print('#{} {}'.format(tc + 1, res))