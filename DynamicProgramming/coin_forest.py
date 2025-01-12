if __name__ == '__main__':

    n = int(input().strip())
    forest = [input().strip() for _ in range(n)]
    # n = 3
    # forest = [
    #     "C.W",
    #     "WC.",
    #     "C.C"
    # ]

    dp = [[-1 for _ in range(3)] for _ in range(n)]
    answer = 0

    for j in range(3):

        if forest[0][j] == 'C':
            dp[0][j] = 1

        elif forest[0][j] == '.':
            dp[0][j] = 0

    for i in range(1, n):

        for j in range(3):

            if forest[i][j] == 'W':
                continue

            for dj in [-1, 0, 1]:
                prev_j = j + dj

                if 0 <= prev_j < 3 and dp[i-1][prev_j] != -1:
                    dp[i][j] = max(dp[i][j], dp[i-1][prev_j] + (1 if forest[i][j] == 'C' else 0))
                    if dp[i][j] > answer:
                        answer = dp[i][j]

    if answer <= 0:
        print(0)

    else:
        print(answer)

    print(dp)

   