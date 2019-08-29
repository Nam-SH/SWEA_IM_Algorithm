import sys; sys.stdin = open('data/(5789)input.txt', 'r')

for tc in range(int(input())):

    N, Q = map(int, input().split())
    arr = [0] * (N + 1)
    for i in range(1, Q + 1):
        l, r = map(int, input().split())
        for j in range(l, r + 1):
            arr[j] = i

    print('#' + str(tc + 1), *arr[1:])
