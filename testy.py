import sys; sys.stdin = open('data/(6485)input.txt', 'r')

for tc in range(int(input())):
    N = int(input())
    arr = [0] * 5001

    for _ in range(N):
        a, b = map(int, input().split())
        for i in range(a, b + 1):
            arr[i] += 1

    print('#' + str(tc + 1), end=' ')
    for _ in range(int(input())):
        print(arr[int(input())], end = ' ')
    print()