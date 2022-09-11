n = int(input())
ans = [[0]*n for i in range(n)]
i, j = 0, 0
k = 0

while k != n*n:
    k += 1
    ans[i][j] = k
    if i + j < n - 1 and i <= j + 1:
        j += 1
    elif j - i > 0:
        i += 1
    elif i + j > n - 1:
        j -= 1
    elif i + j <= n - 1 and i >= j + 1:
        i -= 1

for i in ans:
    print(*i)