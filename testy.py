import sys; sys.stdin = open('data/(6190)input.txt', 'r')

for tc in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    Max = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            val = arr[i] * arr[j]
            if val > 11:
                val = arr[i] * arr[j]
                if val > 11 and len(set(str(val))) >= 2:
                    if list(str(val)) == sorted(list(str(val))):
                        if Max < val:
                            Max = val
    if Max == 0: print('#{} -1'.format(tc + 1))
    else: print('#{} {}'.format(tc + 1, Max))
