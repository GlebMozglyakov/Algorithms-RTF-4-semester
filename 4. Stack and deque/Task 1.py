class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        return "ok"

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop(0)

    def front(self):
        if len(self.items) > 0:
            return self.items[0]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []
        return "ok"

    def view(self):
        return ', '.join(map(str, self.items))


def main():
    queue = Queue()

    while True:
        command = input().split()

        match command[0]:
            case "push":
                print(queue.push(int(command[1])))
            case "pop":
                print(queue.pop())
            case "front":
                print(queue.front())
            case "size":
                print(queue.size())
            case "clear":
                print(queue.clear())
            case "view":
                print(queue.view())
            case "exit":
                print("bye")
                break


if __name__ == "__main__":
    main()
