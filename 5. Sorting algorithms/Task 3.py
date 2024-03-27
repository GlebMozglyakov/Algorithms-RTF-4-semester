def selection_sort(input_array):
    length = len(input_array)
    half_iterations = length // 2 - 1

    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if input_array[j] < input_array[min_index]:
                min_index = j

        input_array[i], input_array[min_index] = input_array[min_index], input_array[i]

        if i == half_iterations:
            intermediate_result = " ".join(map(str, input_array))
            print(intermediate_result)

    return input_array


input_array = list(map(int, input().split()))

sorted_array = selection_sort(input_array)
result = " ".join(map(str, sorted_array))

print(result)
