import sys; sys.stdin = open('data/(1223)input.txt', 'r')

isp = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
icp = {'(': 3, '+': 1, '-': 1, '*': 2, '/': 2}

for tc in range(10):
    N = int(input())

    arr = input()
    sign = []
    res = []
    for i in arr:
        if i.isdigit(): res.append(i)

        else:
            if not sign: sign.append(i)

            else:
                if icp[i] > isp[sign[-1]]: sign.append(i)

                else:
                    while sign and icp[i] <= isp[sign[-1]]: res.append(sign.pop())
                    sign.append(i)

    while sign: res.append(sign.pop())

    calc = []
    for j in res:
        if j.isdigit(): calc.append(j)

        else:
            b = int(calc.pop())
            a = int(calc.pop())

            if j == "+": c = a + b
            else: c = a * b
            calc.append(c)

    print('#{} {}'.format(tc + 1, *calc))