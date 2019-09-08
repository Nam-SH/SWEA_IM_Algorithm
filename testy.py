import sys; sys.stdin = open('data/(1210)input.txt', 'r')

for _ in range(10):
    tc = int(input())
    arr = [input().split() for _ in range(100)]
    y, x = 99, arr[99].index('2')
    d = [-1, 1]

    while y != 0:
        y -= 1
        for i in range(2):
            tx = x + d[i]
            if 0 <= tx < 100 and arr[y][tx] == '1':
                while 0 <= tx < 100 and arr[y][tx] == '1':
                    tx += d[i]
                x = tx
                break

    print('#%d %d' % (tc, x))