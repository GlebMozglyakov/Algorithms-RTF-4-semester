# class TreeNode:
#     def __init__(self, value):
#         self.left = None
#         self.right = None
#         self.value = value
#
#
# class BinaryTree:
#     def build_bst(self, array, start, end):
#         if start > end:
#             return None
#
#         middle = (start + end) // 2
#         node = TreeNode(array[middle])
#         node.left = self.build_bst(array, start, middle - 1)
#         node.right = self.build_bst(array, middle + 1, end)
#
#         return node
#
#     def print_tree(self):
#         lines = self._get_tree_for_print(self.root)
#         for line in lines:
#             print(line)
#
#     def _get_tree_for_print(self, node, prefix="", is_left=None, is_last=True):
#         if node is not None:
#             if is_left is None:
#                 lines = [str(node.value)]
#                 prefix = ""
#             else:
#                 joint = "└───" if is_last else "├───"
#                 lines = [f"{prefix}{joint}{node.value}"]
#                 prefix = prefix + ("    " if is_last else "│   ")
#
#             left_lines = self._get_tree_for_print(node.left, prefix, True, node.right is None)
#             right_lines = self._get_tree_for_print(node.right, prefix, False, True)
#
#             if left_lines:
#                 lines.extend(left_lines)
#             if right_lines:
#                 lines.extend(right_lines)
#
#             return lines
#         else:
#             return []
#
#     def add(self, node, value):
#         if value < node.value:
#             if node.left is None:
#                 node.left = TreeNode(value)
#             else:
#                 self.add(node.left, value)
#         elif value > node.value:
#             if node.right is None:
#                 node.right = TreeNode(value)
#             else:
#                 self.add(node.right, value)
#
#     def delete(self, node, value):
#         if node is None:
#             return None
#
#         if value < node.value:
#             node.left = self.delete(node.left, value)
#         elif value > node.value:
#             node.right = self.delete(node.right, value)
#         else:
#             if node.left is None:
#                 return node.right
#             if node.right is None:
#                 return node.left
#
#             min_larger_node = self._get_min(node.right)
#             node.value = min_larger_node.value
#             node.right = self.delete(node.right, min_larger_node.value)
#
#         return node
#
#     def _get_min(self, node):
#         while node.left is not None:
#             node = node.left
#
#         return node
#
#     def find(self, node, value):
#         if node is None:
#             return False
#
#         if value == node.value:
#             return True
#         elif value < node.value:
#             return self.find(node.left, value)
#         else:
#             return self.find(node.right, value)
#
#     def next(self, value):
#         current = self.root
#         successor = None
#         while current:
#             if current.value > value:
#                 successor = current
#                 current = current.left
#             else:
#                 current = current.right
#
#         return successor
#
#
# tree = BinaryTree()
#
# input_array = list(map(int, input().split()))
#
# tree.root = tree.build_bst(input_array, 0, len(input_array) - 1)
#
# while True:
#     command = input()
#
#     if command == "exit":
#          break
#     elif command.startswith("add "):
#         values = list(map(int, command.split()[1:]))
#
#         for value in values:
#             tree.add(tree.root, value)
#
#         print("Ok")
#     elif command.startswith("delete "):
#         value = int(command.split()[1])
#         tree.delete(tree.root, value)
#
#         print("Ok")
#     elif command.startswith("find "):
#         value = int(command.split()[1])
#
#         print("Число нашлось" if tree.find(tree.root, value) else "Число не нашлось")
#     elif command.startswith("next "):
#         value = int(command.split()[1])
#         result = tree.next(value)
#
#         print(result.value if result else "Следующего числа нет")
#     elif command == "print":
#         tree.print_tree()

# from typing import Optional
#
#
# class TreeNode:
#     def __init__(self, value):
#         self.parent_element = None
#         self.left = None
#         self.right = None
#         self.value = value
#
#     def has_child_element(self):
#         return self.left or self.right
#
#     def is_last_element(self):
#         if self.parent_element:
#             return not (self.parent_element.right_node == self or self.parent_element.right_node is None)
#         return True
#
#     def __str__(self):
#         return str(self.value)
#
#
# class BinaryTree:
#     def __init__(self, root: Optional[TreeNode] = None):
#         self.root: Optional[TreeNode] = root
#
#     def add(self, value):
#         next = self.root
#
#         while next:
#             if value < next.value:
#                 if next.left:
#                     next = next.left
#                 else:
#                     next.left = TreeNode(value)
#                     next.left.parent_element = next
#                     break
#             else:
#                 if next.right:
#                     next = next.right
#                 else:
#                     next.right = TreeNode(value)
#                     next.right.parent_element = next
#                     break
#
#     def delete(self, element):
#         element_for_delete = self.find(element)
#
#         if element_for_delete:
#             self._delete(element_for_delete)
#
#     def _delete(self, element_for_delete):
#         if not element_for_delete.has_child_element():
#             if element_for_delete.parent_element.left_node == element_for_delete:
#                 element_for_delete.parent_element.left_node = None
#             elif element_for_delete.parent_element.right_node == element_for_delete:
#                 element_for_delete.parent_element.right_node = None
#
#             return
#
#         if not (element_for_delete.left_node and element_for_delete.right_node):
#             parent = element_for_delete.parent_element
#             child = element_for_delete.left_node if element_for_delete.left_node else element_for_delete.right_node
#             child.parent_node = parent
#             if parent.left_node == element_for_delete:
#                 parent.left_node = child
#             else:
#                 parent.right_node = child
#             return
#
#         replace_elem = element_for_delete.right_node
#
#         while replace_elem.left_node:
#             replace_elem = replace_elem.left_node
#
#         element_for_delete.value = replace_elem.value
#
#         self._delete(replace_elem)
#
#     def find(self, element) -> Optional[TreeNode]:
#         if not self.root:
#             return None
#
#         return self.__find__(element, self.root)
#
#     def __find__(self, value, node):
#         if value == node.value:
#             return node
#         elif value < node.value and node.left_node:
#             return self.__find__(value, node.left_node)
#         elif value > node.value and node.right_node:
#             return self.__find__(value, node.right_node)
#         return None
#
#     def next(self, value, node=None) -> Optional[TreeNode]:
#         if not node:
#             node = self.find(value)
#
#         if not node:
#             return None
#
#         if node.right:
#             next = node.right
#
#             while next.left_node:
#                 next = next.left_node
#
#             return next
#
#         next = node
#
#         while next.parent_element and next.parent_element.right_node == next:
#             next = next.parent_element
#
#         return next.parent_element
#
#     def build_tree(self, array: list) -> Optional[TreeNode]:
#         if len(array) == 0:
#             return None
#         elif len(array) == 1:
#             return TreeNode(array[0])
#
#         middle = len(array) // 2 - 1 + len(array) % 2
#         center = TreeNode(array[middle])
#         left = self.build_tree(array[:middle])
#         right = self.build_tree(array[middle + 1:])
#
#         if left:
#             center.left = left
#             left.parent_element = center
#
#         if right:
#             center.right = right
#             right.parent_element = center
#
#         return center
#
#     def print_tree(self):
#         result = list()
#         result.append(str(self.root.value))
#
#         prefix = [True]
#         self._get_tree_for_print(prefix, 0, self.root.left, result)
#
#         prefix[0] = False
#         self._get_tree_for_print(prefix, 0, self.root.right, result)
#
#         return "\n".join(result)
#
#     def _get_tree_for_print(self, prefixes, depth, node: TreeNode, result):
#         if node is None:
#             return
#         if len(prefixes) == depth + 1:
#             prefixes.append(True)
#
#         result.append(
#             "".join(['│   ' if i else "    " for i in prefixes[:depth]]) +
#             ("├───" if node.is_last_element() else "└───") +
#             str(node)
#         )
#         if node.left:
#             prefixes[depth + 1] = node.right is not None
#             self._get_tree_for_print(prefixes, depth + 1, node.left, result)
#         prefixes[depth + 1] = False
#         if node.right:
#             self._get_tree_for_print(prefixes, depth + 1, node.right, result)
#
#
# array = list(map(int, input().split()))
# tree = BinaryTree()
# tree.root = tree.build_tree(array)
#
# command = input()
#
# while True:
#     if command.startswith('exit'):
#         break
#     elif command.startswith("print"):
#         print(tree.print_tree())
#     elif command.startswith('add'):
#         values = list(map(int, command.split()[1:]))
#         for value in values:
#             tree.add(value)
#
#         print("Ok")
#     elif command.startswith('delete'):
#         tree.delete(int(command.split()[1]))
#         print('Ok')
#     elif command.startswith('find'):
#         value = int(command.split()[1])
#
#         print("Число нашлось" if tree.find(value) else "Число не нашлось")
#     elif command.startswith('next'):
#         n = tree.next(int(command.split()[1]))
#         if n:
#             print(n.value)
#         else:
#             print("Следующего числа нет")
#
#     command = input()


# from typing import Optional
#
#
# class TreeNode:
#     def __init__(self, value):
#         self.parent_element = None
#         self.left = None
#         self.right = None
#         self.value = value
#
#     def has_child_element(self):
#         return self.left or self.right
#
#     def childs_count(self):
#         return int(self.left is not None) + int(self.right is not None)
#
#     def is_last_element(self):
#         if self.parent_element:
#             return self.parent_element.right_node == self or self.parent_element.childs_count() == 1
#         return False
#
#     def __str__(self):
#         return str(self.value)
#
#
# class BinaryTree:
#     def __init__(self, root: Optional[TreeNode] = None):
#         self.root: Optional[TreeNode] = root
#
#     def add(self, value):
#         next = self.root
#
#         while next:
#             if value < next.value:
#                 if next.left:
#                     next = next.left
#                 else:
#                     next.left = TreeNode(value)
#                     next.left.parent_element = next
#                     break
#             else:
#                 if next.right:
#                     next = next.right
#                 else:
#                     next.right = TreeNode(value)
#                     next.right.parent_element = next
#                     break
#
#     def delete(self, element):
#         element_for_delete = self.find(element)
#
#         if element_for_delete:
#             self._delete(element_for_delete)
#
#     def _delete(self, element_for_delete):
#         if not element_for_delete.has_child_element():
#             if element_for_delete.parent_element.left_node == element_for_delete:
#                 element_for_delete.parent_element.left_node = None
#             elif element_for_delete.parent_element.right_node == element_for_delete:
#                 element_for_delete.parent_element.right_node = None
#
#             return
#
#         if not (element_for_delete.left_node and element_for_delete.right_node):
#             parent = element_for_delete.parent_element
#             child = element_for_delete.left_node if element_for_delete.left_node else element_for_delete.right_node
#             child.parent_node = parent
#             if parent.left_node == element_for_delete:
#                 parent.left_node = child
#             else:
#                 parent.right_node = child
#             return
#
#         replace_elem = element_for_delete.right_node
#
#         while replace_elem.left_node:
#             replace_elem = replace_elem.left_node
#
#         element_for_delete.value = replace_elem.value
#
#         self._delete(replace_elem)
#
#     def find(self, element) -> Optional[TreeNode]:
#         if not self.root:
#             return None
#
#         return self.__find__(element, self.root)
#
#     def __find__(self, value, node):
#         if value == node.value:
#             return node
#         elif value < node.value and node.left_node:
#             return self.__find__(value, node.left_node)
#         elif value > node.value and node.right_node:
#             return self.__find__(value, node.right_node)
#         return None
#
#     def next(self, value, node=None) -> Optional[TreeNode]:
#         if not node:
#             node = self.find(value)
#
#         if not node:
#             return None
#
#         if node.right:
#             next = node.right
#
#             while next.left_node:
#                 next = next.left_node
#
#             return next
#
#         next = node
#
#         while next.parent_element and next.parent_element.right_node == next:
#             next = next.parent_element
#
#         return next.parent_element
#
#     def build_tree(self, array: list) -> Optional[TreeNode]:
#         if len(array) == 0:
#             return None
#         elif len(array) == 1:
#             return TreeNode(array[0])
#
#         middle = len(array) // 2 - 1 + len(array) % 2
#         center = TreeNode(array[middle])
#         left = self.build_tree(array[:middle])
#         right = self.build_tree(array[middle + 1:])
#
#         if left:
#             center.left = left
#             left.parent_element = center
#
#         if right:
#             center.right = right
#             right.parent_element = center
#
#         return center
#
#     def print_tree(self):
#         result = list()
#         result.append(str(self.root.value))
#
#         prefix = [True]
#         self._get_tree_for_print(prefix, 0, self.root.left, result)
#
#         prefix[0] = False
#         self._get_tree_for_print(prefix, 0, self.root.right, result)
#
#         return "\n".join(result)
#
#     def _get_tree_for_print(self, prefixes, depth, node: TreeNode, result):
#         if node is None:
#             return
#         if len(prefixes) == depth + 1:
#             prefixes.append(True)
#
#         result.append(
#             "".join(['│   ' if i else "    " for i in prefixes[:depth]]) +
#             ("└───" if node.is_last_element() else "├───") +
#             str(node)
#         )
#         if node.left:
#             prefixes[depth + 1] = node.right is not None
#             self._get_tree_for_print(prefixes, depth + 1, node.left, result)
#         prefixes[depth + 1] = False
#         if node.right:
#             self._get_tree_for_print(prefixes, depth + 1, node.right, result)
#
#
# array = list(map(int, input().split()))
# tree = BinaryTree()
# tree.root = tree.build_tree(array)
#
# command = input()
#
# while True:
#     if command.startswith('exit'):
#         break
#     elif command.startswith("print"):
#         print(tree.print_tree())
#     elif command.startswith('add'):
#         values = list(map(int, command.split()[1:]))
#         for value in values:
#             tree.add(value)
#
#         print("Ok")
#     elif command.startswith('delete'):
#         tree.delete(int(command.split()[1]))
#         print('Ok')
#     elif command.startswith('find'):
#         value = int(command.split()[1])
#
#         print("Число нашлось" if tree.find(value) else "Число не нашлось")
#     elif command.startswith('next'):
#         n = tree.next(int(command.split()[1]))
#         if n:
#             print(n.value)
#         else:
#             print("Следующего числа нет")
#
#     command = input()


from typing import Optional


class TreeNode:
    def __init__(self, value):
        self.parent_element = None
        self.left_element = None
        self.right_element = None
        self.value = value

    def is_last_element(self):
        if self.parent_element:
            return not (self.parent_element.right_element is None or self.parent_element.right_element == self)

        return True

    def is_has_child_element(self):
        return self.left_element or self.right_element

    def __str__(self):
        return str(self.value)


class BinaryTree:
    def __init__(self, root: Optional[TreeNode] = None):
        self.root: Optional[TreeNode] = root

    def add(self, *args):
        for value in args:
            self._add_value(value)

    def _add_value(self, value):
        if not self.root:
            self.root = TreeNode(value)
            return

        next_element = self.root

        while next_element:
            if value < next_element.value:
                if next_element.left_element:
                    next_element = next_element.left_element
                else:
                    next_element.left_element = TreeNode(value)
                    next_element.left_element.parent_element = next_element
                    break
            else:
                if next_element.right_element:
                    next_element = next_element.right_element
                else:
                    next_element.right_element = TreeNode(value)
                    next_element.right_element.parent_element = next_element
                    break

    def delete(self, value):
        node_for_delete = self.find(value)

        if node_for_delete:
            self._delete_node(node_for_delete)

    def _delete_node(self, node_for_delete):
        if not node_for_delete.is_has_child_element():
            if node_for_delete.parent_element.left_element == node_for_delete:
                node_for_delete.parent_element.left_element = None
            elif node_for_delete.parent_element.right_element == node_for_delete:
                node_for_delete.parent_element.right_element = None

            return

        if not (node_for_delete.left_element and node_for_delete.right_element):
            parent_element = node_for_delete.parent_element

            if node_for_delete.left_element:
                child_element = node_for_delete.left_element
            else:
                child_element = node_for_delete.right_element

            child_element.parent_element = parent_element

            if parent_element.left_element == node_for_delete:
                parent_element.left_element = child_element
            else:
                parent_element.right_element = child_element
            return

        replace_element = node_for_delete.right_element

        while replace_element.left_element:
            replace_element = replace_element.left_element

        node_for_delete.value = replace_element.value

        self._delete_node(replace_element)

    def find(self, value):
        if not self.root:
            return None

        return self._find_node(value, self.root)

    def _find_node(self, value, node):
        if value == node.value:
            return node

        elif node.left_element and value < node.value:
            return self._find_node(value, node.left_element)
        elif node.right_element and value > node.value:
            return self._find_node(value, node.right_element)

        return None

    def next(self, value, node=None):
        if not node:
            node = self.find(value)

        if not node:
            return None

        if node.right_element:
            next = node.right_element

            while next.left_element:
                next = next.left_element

            return next

        next = node

        while next.parent_element and next.parent_element.right_element == next:
            next = next.parent_element

        return next.parent_element

    def build(self, input_array):
        return BinaryTree(self._get_sorted(input_array))

    def _get_sorted(self, array):
        if len(array) == 0:
            return None

        elif len(array) == 1:
            return TreeNode(array[0])

        middle = len(array) // 2 - 1 + len(array) % 2

        center_node = TreeNode(array[middle])
        left = self._get_sorted(array[:middle])
        right = self._get_sorted(array[middle + 1:])

        if left:
            center_node.left_element = left
            left.parent_element = center_node

        if right:
            center_node.right_element = right
            right.parent_element = center_node

        return center_node

    def __str__(self):
        result_print = []

        result_print.append(str(self.root.value))

        pr = [True]

        self._print(pr, 0, self.root.left_element, result_print)

        pr[0] = False

        self._print(pr, 0, self.root.right_element, result_print)

        result = "\n".join(result_print)

        return result

    def _print(self, prefixes, depth, node, result):
        if node is None:
            return

        if len(prefixes) == depth + 1:
            prefixes.append(True)

        result.append(
            "".join(['│   ' if i else "    " for i in prefixes[:depth]]) +
            ("├───" if node.is_last_element() else "└───") +
            str(node)
        )

        if node.left_element:
            prefixes[depth + 1] = node.right_element is not None
            self._print(prefixes, depth + 1, node.left_element, result)

        prefixes[depth + 1] = False

        if node.right_element:
            self._print(prefixes, depth + 1, node.right_element, result)


input_array = list(map(int, input().split()))

tree = BinaryTree()
tree = tree.build(input_array)


command = input()

while True:
    if command == "exit":
         break
    elif command.startswith("add "):
        input_values = list(map(int, command.split()[1:]))
        tree.add(*input_values)

        print("Ok")
    elif command.startswith("delete "):
        value_for_delete = int(command.split()[1])
        tree.delete(value_for_delete)

        print("Ok")
    elif command.startswith("find "):
        value_for_find = int(command.split()[1])

        print("Число нашлось" if tree.find(value_for_find) else "Число не нашлось")
    elif command.startswith("next "):
        value = int(command.split()[1])
        result = tree.next(value)

        print(result.value if result else "Следующего числа нет")
    elif command == "print":
        print(tree)

    command = input()
