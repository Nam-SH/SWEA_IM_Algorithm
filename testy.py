T = int(input())
​
for tc in range(1, T+1):
    N, M, length = map(int, input().split())
    rc = [list(map(int, input().split())) for _ in range(N)]

    for r in range(N - length + 1): # 행 N
        for c in range(M - length + 1): # 열 M
            S = S2 = 0 # 새로운 합을 계속 비교해야하니 0을 계속 할당해준다.
            for i in range(r, r+length):
                for j in range(c, c+length):
                    S += rc[i][j]
            # 작은 사각형도 같은 for문에 돌려주자
            for ii in range(r+1, r+length -1): # 길이는 총 2인덱스가 빠져야 한다.
            # 그래서 양옆을 각각 1더하고 1을 빼면 양옆이 2가 줄어든다.
                for jj in range(c+1, c+length -1):
                    S2 += rc[ii][jj]
            result = S - S2
            if result > Max:
                Max = result
    print('#{} {}'.format(tc, Max))