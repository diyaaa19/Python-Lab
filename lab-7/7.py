class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current_node, key):
        if key < current_node.value:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert_recursive(current_node.left, key)
        else:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert_recursive(current_node.right, key)

    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            print(node.value, end=' ')
            self.in_order_traversal(node.right)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.value == key:
            return node
        if key < node.value:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)


binary_tree = BinaryTree()
values_to_insert = [50, 30, 20, 40, 70, 60, 80]

for value in values_to_insert:
    binary_tree.insert(value)

print("In-order Traversal of the Binary Tree:")
binary_tree.in_order_traversal(binary_tree.root)
print()

search_key = 40
found_node = binary_tree.search(search_key)
if found_node:
    print(f"Node with value {search_key} found in the tree.")
else:
    print(f"Node with value {search_key} not found in the tree.")
