def isDanjo(num):
    while num >= 1:
        num1 = num % 10
        num = num // 10
        num2 = num % 10
        if num2 > num1:
            return False
    return True

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    ans = -1
    for i in range(0, N - 1):
        for j in range(i + 1, N):
            num = nums[i] * nums[j]
            if isDanjo(num):
                if ans < num:
                    ans = num
    print('#%d %d' % (test_case, ans))