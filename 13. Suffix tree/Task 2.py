import sys


class TrieNode:
    def __init__(self):
        self.children_node = {}
        self.is_end_word = False
        self.word_count = 0
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        current = self.root

        for char in word:
            if char not in current.children_node:
                current.children_node[char] = TrieNode()

            current = current.children_node[char]

        current.is_end_word = True
        current.word_count += 1
        current.word = word

        return "ok"

    def get_best_completion(self, prefix):
        current = self.root

        for char in prefix:
            if char not in current.children_node:
                return "None"
            current = current.children_node[char]

        best_word = self._search_best_completion(current)

        return best_word if best_word is not None else "None"

    def _search_best_completion(self, node):
        best_word = None
        max_count = -1
        visit_nodes = [node]

        while visit_nodes:
            current = visit_nodes.pop()

            if current.is_end_word:
                if (current.word_count > max_count or
                            (current.word_count == max_count and len(current.word) < len(best_word)) or
                            (current.word_count == max_count and len(current.word) == len(best_word) and current.word < best_word)):
                    best_word = current.word
                    max_count = current.word_count
            for child in current.children_node.values():
                visit_nodes.append(child)

        return best_word


trie = Trie()

all_input_data = sys.stdin.read().splitlines()

words = all_input_data[0].split()

for word in words:
    trie.add(word)

commands = all_input_data[1:]

for command in commands:
    if command.startswith('+'):
        input_word = command[2:]
        print(trie.add(input_word))
    elif command.startswith('?'):
        input_prefix = command[2:]
        print(trie.get_best_completion(input_prefix))
    elif command.startswith('exit'):
        print('bye')
        break

# words = input().split()
#
# for word in words:
#     trie.add(word)
#
# while True:
#     data = input().split()
#
#     command = data[0]
#
#     if len(data) > 1:
#         input_char = data[1]
#
#     match command:
#         case '+':
#             print(trie.add(input_char))
#         case '?':
#             print(trie.get_best_completion(input_char))
#         case 'exit':
#             print('bye')
#             break
