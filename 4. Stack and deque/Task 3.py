class SpecialQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, knight_id):
        self.queue.append(knight_id)

    def enqueue_middle(self, knight_id):
        middle_position = len(self.queue) // 2 + len(self.queue) % 2

        self.queue.insert(middle_position, knight_id)

    def enqueue_front(self, knight_id):
        self.queue.insert(0, knight_id)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)

        return None


def process_commands(commands):
    queue = SpecialQueue()
    results = []

    for command in commands:
        command = command.split()
        match command[0]:
            case "+":
                queue.enqueue(int(command[1]))
            case "*":
                queue.enqueue_middle(int(command[1]))
            case "!":
                queue.enqueue_front(int(command[1]))
            case "-":
                knight = queue.dequeue()
                if knight is not None:
                    results.append(knight)
    return results


def main():
    n = int(input())
    commands = [input() for _ in range(n)]

    results = process_commands(commands)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
