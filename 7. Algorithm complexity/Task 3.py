def count_bacteria(bacteria_list, temp_list):
    sorted_bacteria = sorted(bacteria_list, key=lambda b: b[0])

    for temp in temp_list:
        low, high = 0, len(sorted_bacteria)
        while low < high:
            mid = (low + high) // 2
            if sorted_bacteria[mid][0] > temp:
                high = mid
            else:
                low = mid + 1
        index = low

        suitable_count = 0
        for j in range(index):
            if sorted_bacteria[j][1] >= temp:
                suitable_count += 1
        yield suitable_count


n = int(input())
bacteria_data = [tuple(map(int, input().split())) for _ in range(n)]
planet_temperatures = list(map(int, input().split()))

results = count_bacteria(bacteria_data, planet_temperatures)

for result in results:
    print(result)
