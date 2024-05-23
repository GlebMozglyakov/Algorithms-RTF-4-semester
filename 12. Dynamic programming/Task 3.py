def get_encode_string(input_string):
    length_string = len(input_string)
    min_encoded = [["" for _ in range(length_string)] for _ in range(length_string)]

    for length in range(1, length_string + 1):
        for start in range(length_string - length + 1):
            end = start + length - 1
            substring = input_string[start:end + 1]
            min_encoded[start][end] = substring

            for k in range(start, end):
                if len(min_encoded[start][k] + min_encoded[k + 1][end]) < len(min_encoded[start][end]):
                    min_encoded[start][end] = min_encoded[start][k] + min_encoded[k + 1][end]

            repeat = find_repeats(substring)

            if repeat:
                times = len(substring) // len(repeat)
                candidate = f"{times}({min_encoded[start][start + len(repeat) - 1]})"

                if len(candidate) < len(min_encoded[start][end]):
                    min_encoded[start][end] = candidate

    result = min_encoded[0][length_string - 1]

    return result


def find_repeats(substring):
    len_substring = len(substring)

    for i in range(1, len_substring):
        repeat = substring[:i]

        if len_substring % i == 0 and repeat * (len_substring // i) == substring:
            return repeat

    return None


input_string = input()
encoded_string = get_encode_string(input_string)
print(encoded_string)
