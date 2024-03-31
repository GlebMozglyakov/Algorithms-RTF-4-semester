def merge(array, temporary, left, middle, right):
    i = left
    j = middle + 1
    k = left
    inv_count = 0

    while i <= middle and j <= right:
        if array[i] >= array[j]:
            temporary[k] = array[i]
            k += 1
            i += 1
            inv_count += (right - j + 1)
        else:
            temporary[k] = array[j]
            k += 1
            j += 1

    while i <= middle:
        temporary[k] = array[i]
        k += 1
        i += 1

    while j <= right:
        temporary[k] = array[j]
        k += 1
        j += 1

    for loop_var in range(left, right + 1):
        array[loop_var] = temporary[loop_var]

    return inv_count


def merge_sort(array, temporary, left, right):
    count = 0

    if left < right:
        middle = (left + right) // 2
        count += merge_sort(array, temporary, left, middle)
        count += merge_sort(array, temporary, middle + 1, right)
        count += merge(array, temporary, left, middle, right)

    return count


def count_inversions(arr):
    temporary = [0] * len(arr)

    return merge_sort(arr, temporary, 0, len(arr) - 1)


N = int(input())
K = [int(input()) for _ in range(N)]

print(count_inversions(K))
