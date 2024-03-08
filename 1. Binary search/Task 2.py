def find_optimal_position(legs, hands):
    length_hands = len(hands)

    right_border = length_hands - 1
    left_border = 0
    middle = left_border + (right_border - left_border) // 2

    while right_border - left_border > 1:
        if legs[middle] < hands[middle]:
            left_border = middle
        else:
            right_border = middle
        middle = left_border + (right_border - left_border) // 2

    c = right_border

    if c == length_hands:
        return length_hands - 1
    elif (max(hands[c - 1], legs[c - 1]) < max(hands[c], legs[c])) and c != 0:
        return c - 1

    while (c < length_hands - 1) and (legs[c] == legs[c + 1]):
        c += 1

    return c


n, m, l = map(int, input().split())

n_lists = [list(map(int, input().split())) for _ in range(n)]
m_lists = [list(map(int, input().split())) for _ in range(m)]
q = int(input())

for _ in range(q):
    i, j = map(int, input().split())

    legs = n_lists[i]
    hands = m_lists[j]

    current_result = find_optimal_position(legs, hands)

    print(current_result)