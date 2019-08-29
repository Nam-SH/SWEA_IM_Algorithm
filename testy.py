import sys; sys.stdin = open('data/(1230)input.txt', 'r')

for tc in range(10):
    basic_n = int(input())
    basic_data = input().split()

    N = int(input())
    data = input().split()

    cnt = i = 0
    while cnt != N:
        if data[i] == 'I':
            x = int(data[i + 1])
            y = int(data[i + 2])
            for j in range(i + 3, i + 3 + y):
                basic_data.insert(x, data[j])
                x += 1
            i += 3 + y

        elif data[i] == 'D':
            x = int(data[i + 1])
            y = int(data[i + 2])
            for _ in range(y):
                basic_data.pop(x)
            i += 3

        elif data[i] == 'A':
            y = int(data[i + 1])
            for j in range(i + 2, i + 2 + y):
                basic_data.append(data[j])
            i += 2

        cnt += 1

    print('#{}'.format(tc + 1), *basic_data[:10])
