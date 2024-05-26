# from collections import deque
#
#
# def get_neighbors(number):
#     neighbors = []
#     number_list = list(number)
#
#     if number_list[0] != '9':
#         new_number = str(int(number_list[0]) + 1) + ''.join(number_list[1:])
#         neighbors.append(new_number)
#
#     if number_list[-1] != '1':
#         new_number = ''.join(number_list[:-1]) + str(int(number_list[-1]) - 1)
#         neighbors.append(new_number)
#
#     new_number = number_list[-1] + ''.join(number_list[:-1])
#     neighbors.append(new_number)
#
#     new_number = ''.join(number_list[1:]) + number_list[0]
#     neighbors.append(new_number)
#
#     return neighbors
#
#
# def bfs_transform(start, target):
#     queue = deque([(start, [start])])
#     visited = set([start])
#
#     while queue:
#         current, path = queue.popleft()
#
#         if current == target:
#             return path
#
#         for neighbor in get_neighbors(current):
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 queue.append((neighbor, path + [neighbor]))
#
#     return []
#
#
# start = input().strip()
# target = input().strip()
#
# if len(start) != len(target):
#     pass
# elif '0' in start or '0' in target:
#     pass
# else:
#     result = bfs_transform(start, target)
#     for num in result:
#         print(num)

from collections import deque


def next(number):
    figures = list(number)
    numbers = []

    if figures[0] != '9':
        new_number = str(int(figures[0]) + 1) + number[1:]
        numbers.append(new_number)

    if figures[-1] != '1':
        new_number = number[:-1] + str(int(figures[-1]) - 1)
        numbers.append(new_number)

    new_number = number[-1] + number[:-1]
    numbers.append(new_number)

    new_number = number[1:] + number[0]
    numbers.append(new_number)

    return numbers


def bfs_shortest_path(start, finish):
    visited = set([start])
    queue = deque([(start, [start])])

    while queue:
        current, path = queue.popleft()

        if current == finish:
            return path

        for next_number in next(current):
            if next_number not in visited:
                visited.add(next_number)
                queue.append((next_number, path + [next_number]))

    return []


start = input()
finish = input()

result_path = bfs_shortest_path(start, finish)

for number in result_path:
    print(number)
