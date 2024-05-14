class Heap:
    def __init__(self):
        self.heap = []

    def add(self, value):
        self.heap.append(value)

        needed_index = len(self.heap) - 1
        parent = (needed_index - 1) // 2

        while needed_index > 0 and self.heap[parent] > self.heap[needed_index]:
            self.heap[parent], self.heap[needed_index] = self.heap[needed_index], self.heap[parent]
            needed_index = parent
            parent = (needed_index - 1) // 2

    def min(self):
        if self.heap:
            return self.heap[0]

    def size(self):
        return len(self.heap)

    def pop(self):
        if self.heap:
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]

            needed_index = 0
            size = len(self.heap)

            while True:
                smallest = needed_index
                left = 2 * needed_index + 1
                right = 2 * needed_index + 2

                if left < size and self.heap[left] < self.heap[smallest]:
                    smallest = left

                if right < size and self.heap[right] < self.heap[smallest]:
                    smallest = right

                if smallest == needed_index:
                    break

                self.heap[smallest], self.heap[needed_index] = self.heap[needed_index], self.heap[smallest]
                needed_index = smallest

            return self.heap.pop()

    def structure(self):
        depth = 0
        index = 0

        while index < len(self.heap):
            next_index = min(len(self.heap), index + (1 << depth))
            print(' '.join(map(str, self.heap[index:next_index])))
            index = next_index
            depth += 1


heap = Heap()

while True:
    input_command = input().split()
    command = input_command[0]

    if len(input_command) > 1:
        input_number = int(input_command[1])

    match command:
        case 'add':
            heap.add(input_number)
            print('ok')
        case 'min':
            print(heap.min())
        case 'size':
            print(heap.size())
        case 'pop':
            print(heap.pop())
        case 'structure':
            print('---STRUCTURE START---')
            heap.structure()
            print('---STRUCTURE END---')
        case 'exit':
            print('bye')
            break
