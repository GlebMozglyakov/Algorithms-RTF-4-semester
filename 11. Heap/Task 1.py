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
        case 'exit':
            print('bye')
            break
