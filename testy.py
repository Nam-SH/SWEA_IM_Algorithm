import sys; sys.stdin = open('data/(1258)input.txt', 'r')


t = int(input())
for tc in range(1):
    n = int(input())
    m = [[0] * n for _ in range(n)]

    dic = dict()
    for i in range(n):
        num = 0
        line = list(map(int, input().split()))
        for j in range(n):
            if line[j]: num += 1
            elif num:
                if num not in dic:
                    dic[num] = 1
                else:
                    dic[num] += 1
                num = 0
    arr = []
    for key in dic:
        arr.append([dic[key], key, dic[key] * key])

    arr.sort(key=lambda x: (x[2], x[0]))

    print("#{} {}".format(tc + 1, len(arr)), end=' ')
    for i in arr: print(i[0], i[1], end = ' ')
    print()