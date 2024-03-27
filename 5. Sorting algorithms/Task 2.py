def insertion_sort(input_array):
    length = len(input_array)
    if length % 2:
        half_iterations = length // 2
    else:
        half_iterations = length // 2 - 1

    for i in range(1, length):
        key = input_array[i]
        j = i - 1

        while j >= 0 and input_array[j] > key:
            input_array[j + 1] = input_array[j]
            j -= 1

        input_array[j + 1] = key

        if i == half_iterations:
            intermediate_result = " ".join(map(str, input_array))
            print(intermediate_result)

    return input_array


input_array = list(map(int, input().split()))

sorted_array = insertion_sort(input_array)
result = " ".join(map(str, sorted_array))

print(result)
