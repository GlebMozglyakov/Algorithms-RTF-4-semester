from collections import deque


class LimitedSizeStack:
    def __init__(self, max_elements):
        self.stack = deque(maxlen=max_elements)
        self.max_elements = max_elements

    def push(self, element):
        self.stack.append(element)
        return "ok"

    def pop(self):
        if len(self.stack) == 0:
            return "Стэк пустой"
        return self.stack.pop()

    def count(self):
        return len(self.stack)


def main():
    max_elements = int(input())
    stack = LimitedSizeStack(max_elements)

    while True:
        command = input().split()

        if command[0] == "push":
            print(stack.push(int(command[1])))
        elif command[0] == "pop":
            print(stack.pop())
        elif command[0] == "count":
            print(stack.count())
        elif command[0] == "exit":
            print("bye")
            break


if __name__ == "__main__":
    main()
