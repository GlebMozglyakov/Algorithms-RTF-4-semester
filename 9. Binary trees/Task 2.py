class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinaryTree:
    def build_bst(self, array, start, end):
        if start > end:
            return None

        middle = (start + end) // 2
        node = TreeNode(array[middle])
        node.left = self.build_bst(array, start, middle - 1)
        node.right = self.build_bst(array, middle + 1, end)

        return node

    def print_tree(self):
        lines = self._get_tree_for_print(self.root)
        for line in lines:
            print(line)

    def _get_tree_for_print(self, node, prefix="", is_left=None, is_last=True):
        if node is not None:
            if is_left is None:
                lines = [str(node.value)]
                prefix = ""
            else:
                joint = "└───" if is_last else "├───"
                lines = [f"{prefix}{joint}{node.value}"]
                prefix = prefix + ("    " if is_last else "│   ")

            left_lines = self._get_tree_for_print(node.left, prefix, True, node.right is None)
            right_lines = self._get_tree_for_print(node.right, prefix, False, True)

            if left_lines:
                lines.extend(left_lines)
            if right_lines:
                lines.extend(right_lines)

            return lines
        else:
            return []

    def add(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self.add(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self.add(node.right, value)

    def delete(self, node, value):
        if node is None:
            return None

        if value < node.value:
            node.left = self.delete(node.left, value)
        elif value > node.value:
            node.right = self.delete(node.right, value)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            min_larger_node = self._get_min(node.right)
            node.value = min_larger_node.value
            node.right = self.delete(node.right, min_larger_node.value)

        return node

    def _get_min(self, node):
        while node.left is not None:
            node = node.left

        return node

    def find(self, node, value):
        if node is None:
            return False

        if value == node.value:
            return True
        elif value < node.value:
            return self.find(node.left, value)
        else:
            return self.find(node.right, value)

    def next(self, value):
        current = self.root
        successor = None
        while current:
            if current.value > value:
                successor = current
                current = current.left
            else:
                current = current.right
        return successor


tree = BinaryTree()

input_array = list(map(int, input().split()))

tree.root = tree.build_bst(input_array, 0, len(input_array) - 1)

while True:
    command = input()

    if command == "exit":
         break
    elif command.startswith("add "):
        values = list(map(int, command.split()[1:]))

        for value in values:
            tree.add(tree.root, value)

        print("Ok")
    elif command.startswith("delete "):
        value = int(command.split()[1])
        tree.delete(tree.root, value)

        print("Ok")
    elif command.startswith("find "):
        value = int(command.split()[1])

        print("Число нашлось" if tree.find(tree.root, value) else "Число не нашлось")
    elif command.startswith("next "):
        value = int(command.split()[1])
        result = tree.next(value)

        print(result.value if result else "Следующего числа нет")
    elif command == "print":
        tree.print_tree()
