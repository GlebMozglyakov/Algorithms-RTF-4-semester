class PrioritizedQueue:
    def __init__(self):
        self.queues = {}
        self.importances = []

    def push(self, i, k):
        if k not in self.queues:
            self.queues[k] = []
            self.importances.append(k)
            self.importances.sort(reverse=True)

        self.queues[k].append(i)

        return "ok"

    def pop(self, k):
        if k == "top":
            if not self.importances:
                return "-1"

            top = self.importances[0]

            k = top
        else:
            k = int(k)

        if k in self.queues and self.queues[k]:
            number = self.queues[k].pop(0)
            if not self.queues[k]:
                del self.queues[k]
                self.importances.remove(k)
            return number

        return "-1"

    def size(self):
        return sum(len(queue) for queue in self.queues.values())

    def popall(self, k):
        if k in self.queues and self.queues[k]:
            numbers = " ".join(map(str, self.queues[k]))
            del self.queues[k]
            self.importances.remove(k)
            return numbers
        else:
            return "-1"

    def clear(self):
        self.queues = {}
        self.importances = []
        return "ok"


def main():
    queue = PrioritizedQueue()

    while True:
        command = input().split()

        match command[0]:
            case "push":
                print(queue.push(int(command[1]), int(command[2])))
            case "pop":
                print(queue.pop(command[1]))
            case "size":
                print(queue.size())
            case "popall":
                print(queue.popall(int(command[1])))
            case "clear":
                print(queue.clear())
            case "exit":
                print("bye")
                break


if __name__ == "__main__":
    main()
