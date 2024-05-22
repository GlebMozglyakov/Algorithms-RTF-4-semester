from typing import Optional


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None
        self.parent_node = None

    def is_last_element(self):
        if self.parent_node:
            return not (self.parent_node.right_node is None or self.parent_node.right_node == self)

        return True

    def get_child_element(self):
        return self.left_node or self.right_node


class BinaryTree:
    def __init__(self, root: Optional[TreeNode] = None):
        self.root: Optional[TreeNode] = root

    def build_binary_tree(self, input_array):
        return BinaryTree(self.__build(input_array))

    def __build(self, array) -> Optional[TreeNode]:
        array_length = len(array)

        if array_length == 0:
            return None

        elif array_length == 1:
            return TreeNode(array[0])

        middle = (array_length // 2) + (array_length % 2) - 1

        center_node = TreeNode(array[middle])

        left = self.__build(array[:middle])
        right = self.__build(array[middle + 1:])

        if left:
            center_node.left_node = left
            left.parent_node = center_node

        if right:
            center_node.right_node = right
            right.parent_node = center_node

        return center_node

    def add(self, *args):
        for value in args:
            self.__add_value(value)

    def __add_value(self, value):
        if not self.root:
            self.root = TreeNode(value)
            return

        next_node = self.root

        while next_node:
            if value < next_node.value:
                if next_node.left_node:
                    next_node = next_node.left_node
                else:
                    next_node.left_node = TreeNode(value)
                    next_node.left_node.parent_node = next_node
                    break
            else:
                if next_node.right_node:
                    next_node = next_node.right_node
                else:
                    next_node.right_node = TreeNode(value)
                    next_node.right_node.parent_node = next_node
                    break

    def delete(self, value):
        value_for_delete = self.find(value)

        if value_for_delete:
            self.__delete_value(value_for_delete)

    def __delete_value(self, value_for_delete):
        if not value_for_delete.get_child_element():
            if value_for_delete.parent_node.left_node == value_for_delete:
                value_for_delete.parent_node.left_node = None
            elif value_for_delete.parent_node.right_node == value_for_delete:
                value_for_delete.parent_node.right_node = None
            return

        if not (value_for_delete.right_node and value_for_delete.left_node):
            parent_node = value_for_delete.parent_node

            if value_for_delete.left_node:
                child_node = value_for_delete.left_node
            else:
                child_node = value_for_delete.right_node

            child_node.parent_node = parent_node

            if parent_node.left_node == value_for_delete:
                parent_node.left_node = child_node
            else:
                parent_node.right_node = child_node

            return

        node_to_replace = value_for_delete.right_node

        while node_to_replace.left_node:
            node_to_replace = node_to_replace.left_node

        value_for_delete.value = node_to_replace.value

        self.__delete_value(node_to_replace)

    def find(self, value):
        if not self.root:
            return None

        return self.__find_node(value, self.root)

    def __find_node(self, value, node):
        if value == node.value:
            return node
        elif node.left_node and value < node.value:
            return self.__find_node(value, node.left_node)
        elif node.right_node and value > node.value:
            return self.__find_node(value, node.right_node)

        return None

    def min(self):
        if not self.root:
            return None

        next_node = self.root

        while next_node.left_node:
            next_node = next_node.left_node

        return next_node.value

    def max(self):
        if not self.root:
            return None

        next_node = self.root

        while next_node.right_node:
            next_node = next_node.right_node

        return next_node.value

    def list(self):
        jars = []

        if self.root:
            self.__get_next_needed_node(self.root, jars)

        return jars

    def __get_next_needed_node(self, node, jars):
        if node.left_node:
            self.__get_next_needed_node(node.left_node, jars)

        jars.append(node.value)

        if node.right_node:
            self.__get_next_needed_node(node.right_node, jars)


input_array = list(map(int, input().split()))

binary_ree = BinaryTree()
binary_ree = binary_ree.build_binary_tree(input_array)
command = input()

while True:
    if command.startswith('add'):
        values = list(map(int, command.split()[1:]))
        binary_ree.add(*values)
        print('Ok')
    elif command.startswith('delete'):
        value_for_delete = int(command.split()[1])
        binary_ree.delete(value_for_delete)
        print('Ok')
    elif command.startswith('find'):
        weight = int(command.split()[1])
        jar = binary_ree.find(weight)
        if jar:
            print('Такая банка есть')
        else:
            print("Такой банки нет")
    elif command.startswith('min'):
        min_value = binary_ree.min()
        if min_value:
            print(min_value)
        else:
            print("Склад пуст")
    elif command.startswith('max'):
        max_value = binary_ree.max()
        if max_value:
            print(max_value)
        else:
            print("Склад пуст")
    elif command.startswith("list"):
        jars = binary_ree.list()
        print(*jars)
    elif command.startswith('exit'):
        break

    command = input()
