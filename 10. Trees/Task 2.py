class Node:
    def __init__(self, index):
        self.index = index
        self.parent_node = None
        self.childs = []


def get_nearest_parent(a, b):
    visited_a_nodes = {a}

    while a.parent_node:
        a = a.parent_node
        visited_a_nodes.add(a)

    visited_b_nodes = {b}

    while len(visited_b_nodes & visited_a_nodes) == 0 and b.parent_node:
        b = b.parent_node
        visited_b_nodes.add(b)

    return b


n = int(input())
s = input()


input_nodes = [Node(i) for i in range(n + 1)]

for data in s[1:-2].split('],'):
    root, nodes = data.strip().split(': [')

    parent_node = input_nodes[int(root)]
    childs = list(map(int, nodes.split(', ')))

    for i in childs:
        child = input_nodes[i]
        parent_node.childs.append(child)
        child.parent_node = parent_node


a, b = map(int, input().split())
a = input_nodes[a]
b = input_nodes[b]

result = get_nearest_parent(a, b)

print(result.index)
