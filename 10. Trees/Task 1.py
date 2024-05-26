class Node:
    def __init__(self, index):
        self.index = index
        self.nodes = []


def get_all_needed_nodes(node, visited_nodes):
    for cur_node in node.nodes:
        if cur_node not in visited_nodes:
            visited_nodes.add(cur_node)
            get_all_needed_nodes(cur_node, visited_nodes)


n, v = map(int, input().split())
adjacent_nodes = [Node(i) for i in range(n)]

for node in adjacent_nodes:
    for i in map(int, input().split()):
        if i == -1:
            continue
        cur = adjacent_nodes[i]
        node.nodes.append(cur)

needed_node = adjacent_nodes[v]

visited_nodes = {needed_node}
get_all_needed_nodes(needed_node, visited_nodes)

result = sorted(visited_nodes, key=lambda e: e.line_index)
result = [x.index for x in result]

print(*result)
