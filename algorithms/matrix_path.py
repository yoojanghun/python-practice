def matrix_path(mat):
    n = len(mat)
    dp = [[0] * n for _ in range(n)]

    def rec(i, j):
        if i < 0 or j < 0:
            return 0
        if dp[i][j] != 0:
            return dp[i][j]
        dp[i][j] = max(rec(i-1, j), rec(i, j-1)) + mat[i][j]
        return dp[i][j]

    return rec(n-1, n-1)


def matrix_path2(mat):
    n = len(mat)
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]) + mat[i - 1][j - 1]

    for row in dp:
        print(row)
    print("최대 합:", dp[n][n])

hello = [
    [6, 7, 12, 5],
    [5, 3, 11, 18],
    [7, 17, 3, 3],
    [8, 10, 14, 9]
]

print(matrix_path(hello))