import sys


class Node:
    __slots__ = ['element', 'previous', 'next']

    def __init__(self, element, previous, next):
        self.element = element
        self.previous = previous
        self.next = next


class LimitedSizeStack:
    def __init__(self, max_elements):
        self.max_elements = max_elements
        self.length = 0
        self.start = None
        self.end = None

    def push(self, element):
        if self.length == self.max_elements:
            if self.start == self.end:
                self.start = None
                self.end = None
            else:
                self.start = self.start.next
                self.start.previous = None
        else:
            self.length += 1

        new_node = Node(element, self.end, None)
        if not self.start:
            self.start = new_node
            self.end = new_node
        else:
            self.end.next = new_node
            self.end = new_node

        return 'ok\n'

    def pop(self):
        if not self.end:
            return

        element = self.end.element

        self.length -= 1

        if not self.end.previous:
            self.start = None
            self.end = None
        else:
            self.end = self.end.previous
            self.end.next = None

        return element

    def count(self):
        if self.length > 0:
            return self.length
        return 0


def main():
    max_elements = int(input())
    stack = LimitedSizeStack(max_elements)

    while True:
        command = input().split()

        match command[0]:
            case 'push':
                sys.stdout.write(stack.push(int(command[1])))
            case 'pop':
                element = stack.pop()
                if element != None:
                    sys.stdout.write(str(element) + '\n')
            case'count':
                sys.stdout.write(str(stack.count()) + '\n')
            case 'exit':
                sys.stdout.write('bye' + '\n')
                break


if __name__ == "__main__":
    main()

# Решение с очередью, которое не проходит по времени,
# потому что кривые тесты
# from collections import deque
#
#
# class LimitedSizeStack:
#     def __init__(self, max_elements):
#         self.stack = deque(maxlen=max_elements)
#         self.max_elements = max_elements
#
#     def push(self, element):
#         self.stack.append(element)
#         return "ok"
#
#     def pop(self):
#         if len(self.stack) == 0:
#             return "Стэк пустой"
#         return self.stack.pop()
#
#     def count(self):
#         return len(self.stack)
#
#
# def main():
#     max_elements = int(input())
#     stack = LimitedSizeStack(max_elements)
#
#     while True:
#         command = input().split()
#
#         match command[0]:
#             case 'push':
#                 print(stack.push(int(command[1])))
#             case 'pop':
#                 print(stack.pop())
#             case'count':
#                 print(stack.count())
#             case 'exit':
#                 print('bye')
#                 break
#
#
# if __name__ == "__main__":
#     main()
