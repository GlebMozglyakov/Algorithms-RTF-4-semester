class TrieNode:
    def __init__(self):
        self.children_node = {}
        self.is_end_word = False


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

        return "ok"

    def get(self, prefix, x):
        current = self.root

        for char in prefix:
            if char not in current.children_node:
                return "empty"

            current = current.children_node[char]

        result = []

        self._collect_words(current, prefix, result)

        filtered_result = [word for word in result if len(word) > len(prefix)]

        if not filtered_result:
            return "empty"

        return " ".join(filtered_result[:x])

    def _collect_words(self, node, prefix, result):
        if node.is_end_word:
            result.append(prefix)

        for char in sorted(node.children_node.keys()):
            self._collect_words(node.children_node[char], prefix + char, result)


trie = Trie()

while True:
    data = input().split()

    command = data[0]

    if len(data) > 1:
        input_string = data[1]

    match command:
        case 'add':
            trie.add(input_string)
            print('ok')
        case 'get':
            x = int(data[2])
            print(trie.get(input_string, x))
        case 'exit':
            print('bye')
            break
