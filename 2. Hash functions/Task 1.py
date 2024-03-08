first_arr = list(map(int, input().split()))
second_arr = list(map(int, input().split()))

counts = {}
for el in second_arr:
    if el in counts:
        counts[el] += 1
    else:
        counts[el] = 1

results = [str(counts.get(element, 0)) for element in first_arr]

print(' '.join(results))
