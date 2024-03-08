def find_optimal_position(value, n):
    left_count = 0
    right_count = n.count(value)

    non_equal_right = len(n) - right_count
    optimal_product = 0

    for el in n:
        if el == value:
            left_count += 1
            right_count -= 1
        else:
            non_equal_right -= 1
        optimal_product = max(optimal_product, left_count * non_equal_right)

    return optimal_product


n = list(map(int, input().split()))
m = list(map(int, input().split()))

calculated_results = {}
final_output = []

for value in m:
    if value not in calculated_results:
        calculated_results[value] = find_optimal_position(value, n)
    final_output.append(calculated_results[value])

print(' '.join(map(str, final_output)))
