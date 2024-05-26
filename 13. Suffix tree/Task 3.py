# from collections import deque, defaultdict
# import sys
#
#
# class AhoCorasickNode:
#     def __init__(self):
#         self.children = {}
#         self.fail = None
#         self.output = []
#
#
# class AhoCorasickAutomat:
#     def __init__(self):
#         self.root = AhoCorasickNode()
#
#
#     def build(self):
#         queue = deque()
#
#         for child in self.root.children.values():
#             child.fail = self.root
#             queue.append(child)
#
#         while queue:
#             current = queue.popleft()
#
#             for key, child in current.children.items():
#                 fail_node = current.fail
#
#                 while fail_node and key not in fail_node.children:
#                     fail_node = fail_node.fail
#
#                 if fail_node:
#                     child.fail = fail_node.children[key]
#                 else:
#                     child.fail = self.root
#
#                 child.output += child.fail.output
#                 queue.append(child)
#
#     def add_word(self, word):
#         node = self.root
#
#         for char in word:
#             if char not in node.children:
#                 node.children[char] = AhoCorasickNode()
#
#             node = node.children[char]
#
#         node.output.append(word)
#
#
#
#     def search(self, text):
#         node = self.root
#
#         for i, char in enumerate(text):
#             while node and char not in node.children:
#                 node = node.fail
#
#             if node:
#                 node = node.children[char]
#
#                 if node.output:
#                     for pattern in node.output:
#                         yield i - len(pattern) + 1, pattern
#             else:
#                 node = self.root
#
#
# automat = AhoCorasickAutomat()
#
# all_input_data = sys.stdin.read().splitlines()
#
# n = int(all_input_data[0])
# forbidden_words = all_input_data[1:n + 1]
# m = int(all_input_data[n + 1])
# text_lines = all_input_data[n + 2:n + 2 + m]
#
# for word in forbidden_words:
#     automat.add_word(word)
#
# automat.build()
#
# for line_idx, line in enumerate(text_lines):
#     flag = False
#     for pos, word in automat.search(line):
#         print(f"{line_idx + 1} {pos + 1}")
#         flag = True
#         break
#     if flag:
#         break
#
# if not flag:
#     print("Одобрено")

from collections import deque
import sys


class AhoCorasickAutomat:
    def __init__(self):
        self.edges = [{}]
        self.output = [[]]
        self.fails = [-1]
        self.nodes_count = 1

    def build(self):
        queue = deque()

        for ch in self.edges[0]:
            needed_node = self.edges[0][ch]
            self.fails[needed_node] = 0

            queue.append(needed_node)

        while queue:
            current_node = queue.popleft()

            for ch, needed_node in self.edges[current_node].items():
                fail_node = self.fails[current_node]

                while ch not in self.edges[fail_node] and fail_node != -1:
                    fail_node = self.fails[fail_node]

                if fail_node == -1:
                    self.fails[needed_node] = 0
                else:
                    self.fails[needed_node] = self.edges[fail_node][ch]
                    self.output[needed_node].extend(self.output[self.fails[needed_node]])

                queue.append(needed_node)

    def add(self, input_word):
        current = 0

        for ch in input_word:
            if ch not in self.edges[current]:
                self.edges[current][ch] = self.nodes_count
                self.edges.append({})

                self.nodes_count += 1
                self.output.append([])
                self.fails.append(-1)

            current = self.edges[current][ch]

        self.output[current].append(input_word)

    def find_forbidden_words(self, input_text):
        current = 0

        for i in range(len(input_text)):
            while input_text[i] not in self.edges[current] and current != -1:
                current = self.fails[current]

            if current == -1:
                current = 0
                continue

            current = self.edges[current][input_text[i]]

            if self.output[current]:
                return i - len(self.output[current][0]) + 2, i + 1

        return None


automat = AhoCorasickAutomat()

all_input_data = sys.stdin.read().splitlines()

n = int(all_input_data[0])
forbidden_words = [all_input_data[i + 1].lower() for i in range(n)]
m = int(all_input_data[n + 1])
text = [all_input_data[n + 2 + i].lower() for i in range(m)]

for word in forbidden_words:
    automat.add(word)

automat.build()

is_not_word = True

for i in range(m):
    result = automat.find_forbidden_words(text[i])
    if result:
        print(f"{i + 1} {result[0]}")
        is_not_word = False
        break

if is_not_word:
    print("Одобрено")
