n, m = map(int, input().split())
tiles = list(map(int, input().split()))

final_k = []

for k in range(1, n//2 +1):
    if tiles[k] == tiles[k - 1] and tiles[:k] == list(reversed(tiles[k:2 * k])):
        final_k.append(k)

print(*final_k)