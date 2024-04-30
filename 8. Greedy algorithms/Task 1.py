def get_max_cakes(w, cakes):
    cakes.sort(key=lambda x: x[0] / x[1], reverse=True)

    total_sum = 0.0

    for price, size in cakes:
        if size <= w:
            total_sum += price
            w -= size
        else:
            total_sum += (price / size) * w
            break

    return total_sum


n, w = map(int, input().split())
cakes = []

for _ in range(n):
    p, s = map(int, input().split())
    cakes.append((p, s))

result = get_max_cakes(w, cakes)

print(f"{result:.2f}")
