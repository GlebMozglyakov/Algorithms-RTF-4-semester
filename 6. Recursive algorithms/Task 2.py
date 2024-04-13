def generate_score_sequences(sequences, position, n, m, result):
    if position == len(sequences):
        print(*sequences)
        result[0] += 1

        return

    if n - m < len(sequences) - position - 1:
        return

    for val in range(m, n + 1):
        sequences[position] = val
        generate_score_sequences(sequences, position + 1, val - 1, m, result)


k, m, n = map(int, input().split())

all_sequences = [0] * k
result = [0]
generate_score_sequences(all_sequences, 0, n, m, result)

print(result[0])
