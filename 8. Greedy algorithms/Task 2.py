import heapq
from collections import defaultdict

def calculate_huffman_code_length(message):
    # Считаем частоту символов в сообщении
    frequency = defaultdict(int)
    for char in message:
        frequency[char] += 1

    # Создаем мин-кучу
    heap = [(freq, 0, char) for char, freq in frequency.items()]
    heapq.heapify(heap)

    if len(heap) == 1:
        return frequency[heap[0][2]]  # Все символы будут иметь один и тот же код

    # Строим дерево Хаффмана
    while len(heap) > 1:
        freq1, type1, left = heapq.heappop(heap)
        freq2, type2, right = heapq.heappop(heap)
        heapq.heappush(heap, (freq1 + freq2, 1, (left, right)))

    # Функция для генерации кодов Хаффмана
    def generate_codes(node, path=""):
        if isinstance(node, str):
            return {node: path}
        left, right = node
        codes = {}
        codes.update(generate_codes(left, path + '0'))
        codes.update(generate_codes(right, path + '1'))
        return codes

    # Получаем корень дерева
    _, _, root = heap[0]

    # Генерация кодов Хаффмана
    huffman_codes = generate_codes(root)

    # Вычисляем длину закодированного сообщения
    encoded_length = sum(len(huffman_codes[char]) * frequency[char] for char in message)

    return encoded_length

# Тестирование
input_message = "abbccc"
print(calculate_huffman_code_length(input_message))  # Ожидаем увидеть 9
