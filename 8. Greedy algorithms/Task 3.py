def get_max_count_gymnasts(gymnasts):
    needed_gymnasts = [gymnasts[0]]
    gymnasts = gymnasts[1:]
    total_weight = needed_gymnasts[0][2]

    for gymnast in gymnasts:
        if total_weight <= gymnast[1]:
            total_weight += gymnast[2]
            needed_gymnasts.append(gymnast)
            continue

        ind = needed_gymnasts.index(max(needed_gymnasts, key=lambda x: x[2]))

        if needed_gymnasts[ind][2] > gymnast[2]:
            total_weight += gymnast[2]
            total_weight -= needed_gymnasts[ind][2]
            needed_gymnasts[ind] = gymnast

    return len(needed_gymnasts)


n = int(input())

gymnasts = []

for _ in range(n):
    input_string = input().split(';')
    name, max_weight, weight = input_string[0], int(input_string[1]), int(input_string[2])
    gymnasts.append((name, max_weight, weight))

gymnasts = sorted(gymnasts, key=lambda x: (-(x[1] + x[2]), x[2]), reverse=True)

result = get_max_count_gymnasts(gymnasts)

print(result)
