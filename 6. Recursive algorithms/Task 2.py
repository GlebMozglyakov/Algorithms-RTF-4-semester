# def generate_score_sequences(start, end, length, current_score_sequences, score_sequences):
#     if length == 0:
#         score_sequences.append(current_score_sequences)
#         return
#
#     for i in range(start, end + 1):
#         generate_score_sequences(i + 1, end, length - 1, current_score_sequences + [i], score_sequences)
#
#
# k, m, n = map(int, input().split())
#
# score_sequences = []
# current_score_sequences = []
# generate_score_sequences(m, n, k, current_score_sequences, score_sequences)
#
# for sequence in score_sequences:
#     sequence.reverse()
#
# score_sequences.sort()
#
# for sequence in sorted(score_sequences):
#     print(' '.join(map(str, sequence)))
#
# print(len(score_sequences))


def generate_score_sequences(start, end, length, current_score_sequence, score_sequences):
    if length == 0:
        score_sequences.append(current_score_sequence.copy())
        return

    for i in range(start, end + 1):
        current_score_sequence.append(i)
        generate_score_sequences(i + 1, end, length - 1, current_score_sequence, score_sequences)
        current_score_sequence.pop()


k, m, n = map(int, input().split())

score_sequences = []
generate_score_sequences(m, n, k, [], score_sequences)

for sequence in score_sequences:
    sequence.reverse()

score_sequences.sort()

for sequence in score_sequences:
    print(' '.join(map(str, sequence)))

print(len(score_sequences))
