class Heap:
    def __init__(self):
        self.heap = []

    def add(self, value):
        self.heap.append(value)

        needed_index = len(self.heap) - 1
        parent = (needed_index - 1) // 2

        while needed_index > 0 and self.heap[parent] < self.heap[needed_index]:
            self.heap[parent], self.heap[needed_index] = self.heap[needed_index], self.heap[parent]
            needed_index = parent
            parent = (needed_index - 1) // 2

    def pop(self):
        if not self.heap:
            return None

        root_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        needed_index = 0
        size = len(self.heap)

        while True:
            largest = needed_index
            left = 2 * needed_index + 1
            right = 2 * needed_index + 2

            if left < size and self.heap[left] > self.heap[largest]:
                largest = left
            if right < size and self.heap[right] > self.heap[largest]:
                largest = right

            if largest == needed_index:
                break

            self.heap[needed_index], self.heap[largest] = self.heap[largest], self.heap[needed_index]
            needed_index = largest

        return root_value

    def size(self):
        return len(self.heap)


n, w = map(int, input().split())
cakes = [(map(int, input().split())) for _ in range(n)]

heap = Heap()

for p, s in cakes:
    if s > 0:
        heap.add((p / s, p, s))

total_value = 0.0
current_weight = 0

while current_weight < w and heap.size() > 0:
    cost, price, weight = heap.pop()
    if current_weight + weight <= w:

        total_value += price
        current_weight += weight
    else:
        can_take = w - current_weight
        total_value += (price / weight) * can_take
        current_weight = w

print(f"{total_value:.2f}")
