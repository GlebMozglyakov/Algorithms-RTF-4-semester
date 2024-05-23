# def knapsack(n, W, items):
#     integer_cakes = []
#     fractional_cakes = []
#
#     for p, s, q in items:
#         if q == 'Н':
#             integer_cakes.append((p, s))
#         else:
#             fractional_cakes.append((p, s))
#
#     # Динамическое программирование для целых тортов
#     dp = [0] * (W + 1)
#     for p, s in integer_cakes:
#         for w in range(W, s - 1, -1):
#             dp[w] = max(dp[w], dp[w - s] + p)
#
#     # Жадный алгоритм для дробных тортов
#     fractional_cakes.sort(key=lambda x: x[0] / x[1], reverse=True)
#     max_value = max(dp)
#     remaining_capacity = W
#
#     for p, s in fractional_cakes:
#         if remaining_capacity >= s:
#             max_value += p
#             remaining_capacity -= s
#         else:
#             max_value += p * (remaining_capacity / s)
#             break
#
#     return round(max_value, 2)
#
#
# n, w = map(int, input().split())
# cakes = [input().split() for _ in range(n)]
# cakes = [(int(c[0]), int(c[1]), c[2]) for c in cakes]
#
# result = knapsack(n, w, cakes)
# print(result)


def help_for_recedevist(w, cakes):
    cakes.sort(key=lambda x: x[3], reverse=True)

    total_sum = 0
    remaining = w

    for p, s, can_cut, value_per_unit in cakes:
        if remaining == 0:
            break
        if can_cut == 'Д':
            if remaining >= s:
                total_sum += p
                remaining -= s
            else:
                total_sum += value_per_unit * remaining
                remaining = 0
        else:
            if remaining >= s:
                total_sum += p
                remaining -= s

    result = "{:.2f}".format(total_sum)

    return result


n, w = map(int, input().split())
cakes = []

for i in range(n):
    p, s, q = input().split()
    p = int(p)
    s = int(s)
    value_per_unit = p / s
    cakes.append((p, s, q, value_per_unit))


print(help_for_recedevist(w, cakes))
