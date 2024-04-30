def find_k_statistics(array, k):
    if len(array) == 1:
        return array[0]

    point = array[-1]

    right_side = list()

    for i in array:
        if i > point:
            right_side.append(i)

    left_side = list()

    for i in array:
        if i < point:
            left_side.append(i)

    m_count = len(array) - len(right_side) - len(left_side)
    middle = [point] * m_count

    if k < len(left_side):
        return find_k_statistics(left_side, k)
    elif k < len(left_side) + len(middle):
        return middle[0]
    else:
        return find_k_statistics(right_side, k - len(left_side) - len(middle))


input_array = list(map(int, input().split()))
k = int(input())

print(find_k_statistics(input_array, k))
