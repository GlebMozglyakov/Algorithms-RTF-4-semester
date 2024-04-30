# def partition(numbers, left, right):
#     if right - left <= 1:
#         return left
#
#     i = left
#     j = right - 2
#     support_element = numbers[right - 1]
#     print(support_element)
#
#     while i <= j:
#         while numbers[i] < support_element:
#             i += 1
#
#         while numbers[j] >= support_element and j >= i:
#             j -= 1
#
#         if i <= j:
#             numbers[i], numbers[j] = numbers[j], numbers[i]
#
#     numbers[i], numbers[right - 1] = numbers[right - 1], numbers[i]
#     return i
#
#
# def quick_sort(numbers, left, right):
#     if right - left <= 0:
#         return
#
#     m = partition(numbers, left, right)
#
#     quick_sort(numbers, left, m)
#     quick_sort(numbers, m + 1, right)
#
#
# def main():
#     numbers = list(map(int, input().split()))
#     quick_sort(numbers, 0, len(numbers))
#     print(' '.join(map(str, numbers)))
#
#
# main()


# def divide(arr, low, high):
#     if high - low <= 1:
#         return low
#
#     pointer_left = low
#     pointer_right = high - 2
#     pivot = arr[high - 1]
#
#     print(pivot)
#
#     while pointer_left <= pointer_right:
#         while arr[pointer_left] < pivot:
#             pointer_left += 1
#
#         while arr[pointer_right] >= pivot and pointer_right >= pointer_left:
#             pointer_right -= 1
#
#         if pointer_left <= pointer_right:
#             arr[pointer_left], arr[pointer_right] = arr[pointer_right], arr[pointer_left]
#
#     arr[pointer_left], arr[high - 1] = arr[high - 1], arr[pointer_left]
#     return pointer_left


def quick_sort_with_last_element(arr, low, high):
    if high - low <= 0:
        return
    elif high - low <= 1:
        return low

    pointer_left = low
    pointer_right = high - 2
    pivot = arr[high - 1]

    print(pivot)

    while pointer_left <= pointer_right:
        while arr[pointer_left] < pivot:
            pointer_left += 1

        while arr[pointer_right] >= pivot and pointer_right >= pointer_left:
            pointer_right -= 1

        if pointer_left <= pointer_right:
            arr[pointer_left], arr[pointer_right] = arr[pointer_right], arr[pointer_left]

    arr[pointer_left], arr[high - 1] = arr[high - 1], arr[pointer_left]

    partition_index = pointer_left

    quick_sort_with_last_element(arr, low, partition_index)
    quick_sort_with_last_element(arr, partition_index + 1, high)


input_numbers = list(map(int, input().split()))

start_low = 0
start_high = len(input_numbers)

quick_sort_with_last_element(input_numbers, start_low, start_high)

print(*input_numbers)