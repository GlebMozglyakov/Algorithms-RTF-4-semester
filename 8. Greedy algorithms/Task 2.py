import heapq
from collections import Counter


class Node:
    def __init__(self, value=None, weight=0):
        self.value = value
        self.weight = weight
        self.left_node = None
        self.right_node = None

    def __lt__(self, other_node):
        return self.weight < other_node.weight


class HuffmanAlgorithm:
    def __init__(self, symbols_count):
        self.root = None
        self.generate_tree(symbols_count)

    def generate_tree(self, symbols_count):
        heap = []

        for symbol, weight in symbols_count.items():
            heap.append(Node(symbol, weight))

        heapq.heapify(heap)

        while len(heap) > 1:
            n1 = heapq.heappop(heap)
            n2 = heapq.heappop(heap)

            merged_weights = Node(weight=n1.weight + n2.weight)

            merged_weights.left_node = n1
            merged_weights.right_node = n2

            heapq.heappush(heap, merged_weights)

        self.root = heap[0]

    def get_codes(self):
        needed_codes = {}
        self._rec_codes(self.root, '', needed_codes)

        return needed_codes

    def _rec_codes(self, node, code, needed_codes):
        if node.value:
            needed_codes[node.value] = code
        else:
            self._rec_codes(node.left_node, code + '0', needed_codes)
            self._rec_codes(node.right_node, code + '1', needed_codes)


input_string = input()

symbols_count = dict(Counter(input_string))

if len(symbols_count) == 1:
    print(len(input_string))
else:
    huffman = HuffmanAlgorithm(symbols_count)
    codes = huffman.get_codes()

    result = ''.join(codes[symbol] for symbol in input_string)

    print(len(result))
