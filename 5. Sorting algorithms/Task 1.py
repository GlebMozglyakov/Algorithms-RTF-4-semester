def bubble_sort(input_array, k):
    length = len(input_array)

    for i in range(length):
        if i == k:
            intermediate_result = " ".join(map(str, input_array))
            print(intermediate_result)

        for j in range(0, length - i - 1):
            if input_array[j] > input_array[j+1]:
                input_array[j], input_array[j+1] = input_array[j+1], input_array[j]

    return input_array


input_array = list(map(int, input().split()))
k = int(input())

sorted_array = bubble_sort(input_array, k)
result = " ".join(map(str, sorted_array))

print(result)
