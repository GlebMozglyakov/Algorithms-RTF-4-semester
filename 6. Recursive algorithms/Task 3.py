def find_best_combo(n, w, menu, index=0, memo={}):
    if index == n or w == 0:
        return (0, [], 0)

    if (index, w) in memo:
        return memo[(index, w)]

    best_without = find_best_combo(n, w, menu, index + 1, memo)

    if menu[index][0] <= w:
        cals_with, combo_with, cost_with = find_best_combo(n, w - menu[index][0], menu, index + 1, memo)
        cals_with += menu[index][1]
        cost_with += menu[index][0]

        if (cals_with > best_without[0] or
            (cals_with == best_without[0] and len(combo_with) + 1 > len(best_without[1])) or
            (cals_with == best_without[0] and len(combo_with) + 1 == len(best_without[1]) and [index] + combo_with < best_without[1])):
            memo[(index, w)] = (cals_with, [index] + combo_with, cost_with)
            return memo[(index, w)]

    memo[(index, w)] = best_without
    return best_without


n, w = map(int, input().split())

menu = []

for _ in range(n):
    p, c = map(int, input().split())
    menu.append((p, c))

cals, combo, cost = find_best_combo(n, w, menu)

print(f"{len(combo)} {cals}")
print(" ".join(map(str, [i + 1 for i in combo])))
