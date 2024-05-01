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
            if is_left is None:  # корень дерева
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


tree = BinaryTree()

input_array = list(map(int, input().split()))

tree.root = tree.build_bst(input_array, 0, len(input_array) - 1)
tree.print_tree()
