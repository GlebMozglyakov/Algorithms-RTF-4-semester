# class StringGenerator:
#     def __init__(self, weights, input_string):
#         self.weights = weights
#         self.input_string = input_string
#         self.chars_count = self._get_chars_count()
#
#     def generate_string(self):
#         string = self._get_string()
#         weight = self._get_weight(string)
#
#         return string, weight
#
#     def _get_string(self):
#         chars_twice = [
#             char for char in sorted(self.chars_count, key=lambda char: (self.weights[char], -ord(char)))
#             if self.chars_count[char] >= 2 and self.weights[char] > 0
#         ]
#
#         chars_other = [
#             char for char in sorted(self.chars_count)
#             if self.chars_count[char] != 2
#         ]
#
#         word_parts = [
#             char * (self.chars_count[char] if self.weights[char] == 0 else max(1, self.chars_count[char] - 2))
#             for char in chars_other
#         ]
#
#         string = "".join(word_parts)
#
#         for char in chars_twice:
#             string = char + string + char
#
#         return string
#
#     def _get_weight(self, string):
#         return sum(
#             (string.rfind(char) - string.find(char)) * self.weights[char]
#             for char in self.chars_count
#         )
#
#     def _get_chars_count(self):
#         return {char: self.input_string.count(char) for char in set(self.input_string)}
#
#
# input_string = input()
# weights_input = input().split()
#
# alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
#
# weights = {alphabet[i]: int(weight) for i, weight in enumerate(weights_input)}
#
# generator = StringGenerator(weights, input_string)
# word, weight = generator.generate_string()
#
# print(f"{word} {weight}")


class StringGenerator:
    def __init__(self, weights, input_string):
        self.weights = weights
        self.input_string = input_string

    def generate_string(self):
        chars_count = self._get_chars_count()
        string = self._get_string(chars_count)
        weight = self._get_weight(chars_count, string)

        return string, weight

    def _get_string(self, chars_count):
        chars_twice = sorted(filter(
                lambda char: chars_count[char] >= 2 and self.weights[char] > 0,
                chars_count.keys()
            ), key=lambda char: (self.weights[char], -ord(char)))

        chars_other = sorted(filter(
                lambda char: chars_count[char] != 2,
                chars_count.keys()
            ), key=lambda char: ord(char))

        string = ""

        for char in chars_other:
            if self.weights[char] == 0:
                string += char * chars_count[char]
            else:
                string += char * max(1, chars_count[char] - 2)

        for char in chars_twice:
            string = char + string + char

        return string

    def _get_weight(self, chars_count, string):
        weight = 0

        for char in chars_count.keys():
            weight += (string.rfind(char) - string.find(char)) * self.weights[char]

        return weight

    def _get_chars_count(self):
        chars_count = {}

        for char in self.input_string:
            if char not in chars_count:
                chars_count[char] = 0

            chars_count[char] += 1

        return chars_count


input_string = input()
weights = dict()
weights_input = input().split()

for i in range(1072, 1104):
    weights[chr(i)] = int(weights_input[i - 1072])

generator = StringGenerator(weights, input_string)
word, weight = generator.generate_string()

print(f"{word} {weight}")
