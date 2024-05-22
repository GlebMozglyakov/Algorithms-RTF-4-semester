def get_max_coins(n, m, coins):
    prev_row = [0] * m
    current_row = [0] * m

    current_row[0] = coins[0][0]

    for i in range(1, m):
        current_row[i] = current_row[i - 1] + coins[0][i]

    for i in range(1, n):
        prev_row, current_row = current_row, [0] * m

        current_row[0] = prev_row[0] + coins[i][0]

        for j in range(1, m):
            current_row[j] = coins[i][j] + max(prev_row[j], current_row[j - 1])

    max_coins = current_row[m - 1]

    return max_coins


n, m = map(int, input().split())
coins = [list(map(int, input().split())) for _ in range(n)]

max_coins = get_max_coins(n, m, coins)

print(max_coins)
