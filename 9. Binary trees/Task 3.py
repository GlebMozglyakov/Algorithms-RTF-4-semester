from typing import Optional


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

    def has_child(self):
        return self.left or self.right

    def is_last(self):
        if self.parent:
            return not (self.parent.right_node == self or self.parent.right_node is None)
        return True

    def __str__(self):
        return str(self.value)


class Tree:
    def __init__(self, root: Optional[TreeNode] = None):
        self.root: Optional[TreeNode] = root

    def to_sorted_list(self):
        result = []
        if self.root:
            self.__walk__(self.root, result)
        return result

    def min(self):
        if not self.root:
            return None
        nxt = self.root
        while nxt.left:
            nxt = nxt.left
        return nxt.value

    def max(self):
        if not self.root:
            return None
        nxt = self.root
        while nxt.right:
            nxt = nxt.right
        return nxt.value

    def __walk__(self, node, result):
        if node.left_node:
            self.__walk__(node.left_node, result)
        result.append(node.value)
        if node.right_node:
            self.__walk__(node.right_node, result)

    def delete(self, elem):
        to_delete = self.find(elem)
        if to_delete:
            self.__delete_node__(to_delete)

    def __delete_node__(self, to_delete):
        if not to_delete.has_child():
            if to_delete.parent_node.left_node == to_delete:
                to_delete.parent_node.left_node = None
            elif to_delete.parent_node.right_node == to_delete:
                to_delete.parent_node.right_node = None
            return

        if not (to_delete.left_node and to_delete.right_node):
            par = to_delete.parent_node
            child = to_delete.left_node if to_delete.left_node else to_delete.right_node
            child.parent_node = par
            if par.left_node == to_delete:
                par.left_node = child
            else:
                par.right_node = child
            return

        replace_elem = to_delete.right_node
        while replace_elem.left_node:
            replace_elem = replace_elem.left_node

        to_delete.value = replace_elem.value
        self.__delete_node__(replace_elem)

    def next(self, elem, node=None) -> Optional[TreeNode]:
        if not node:
            node = self.find(elem)
        if not node:
            return None

        if node.right:
            nxt = node.right
            while nxt.left_node:
                nxt = nxt.left_node
            return nxt

        nxt = node
        while nxt.parent and nxt.parent.right_node == nxt:
            nxt = nxt.parent
        return nxt.parent

    def find(self, elem) -> Optional[Node]:
        if not self.root:
            return None

        return self.__find__(elem, self.root)

    def __find__(self, elem, node):
        if elem == node.value:
            return node
        elif elem < node.value and node.left_node:
            return self.__find__(elem, node.left_node)
        elif elem > node.value and node.right_node:
            return self.__find__(elem, node.right_node)
        return None

    def add(self, *args):
        for elem in args:
            self.__add_elem__(elem)

    def __add_elem__(self, element):
        if not self.root:
            self.root = Node(element)
            return

        next = self.root
        while next:
            if element < next.value:
                if next.left:
                    next = next.left
                else:
                    next.left = Node(element)
                    next.left.parent_node = next
                    break
            else:
                if next.right:
                    next = next.right
                else:
                    next.right = Node(element)
                    next.right.parent_node = next
                    break

    @classmethod
    def from_sorted_arr(cls, arr: list):
        return Tree(cls.__from_sorted(arr))

    @classmethod
    def __from_sorted(cls, arr: list) -> Optional[TreeNode]:
        if len(arr) == 0:
            return None
        elif len(arr) == 1:
            return TreeNode(arr[0])

        mid = len(arr) // 2 - 1 + len(arr) % 2
        center = TreeNode(arr[mid])
        left = cls.__from_sorted(arr[:mid])
        right = cls.__from_sorted(arr[mid + 1:])
        if left:
            center.left = left
            left.parent = center
        if right:
            center.right = right
            right.parent = center
        return center


t = Tree.from_sorted_arr(list(map(int, input().split())))
command = input()
while True:
    if command.startswith("list"):
        print(*t.to_sorted_list())
    elif command.startswith('exit'):
        break
    elif command.startswith('add'):
        args = list(map(int, command.split()[1:]))
        t.add(*args)
        print('Ok')
    elif command.startswith('delete'):
        t.delete(int(command.split()[1]))
        print('Ok')
    elif command.startswith('find'):
        n = t.find(int(command.split()[1]))
        if n:
            print('Такая банка есть')
        else:
            print("Такой банки нет")
    elif command.startswith('min'):
        m = t.min()
        print(m if m else "Склад пуст")
    elif command.startswith('max'):
        m = t.max()
        print(m if m else "Склад пуст")
    command = input()
