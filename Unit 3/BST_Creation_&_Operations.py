
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Insert a node into BST
def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    return root


# Level order traversal
def level_order(root):
    if root is None:
        return

    queue = [root]

    while queue:
        current = queue.pop(0)
        print(current.data, end=" ")

        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)


# Calculate height of BST
def height(root):
    if root is None:
        return 0

    left_height = height(root.left)
    right_height = height(root.right)

    return 1 + max(left_height, right_height)


# Identify leaf nodes
def leaf_nodes(root):
    if root is None:
        return

    if root.left is None and root.right is None:
        print(root.data, end=" ")
        return

    leaf_nodes(root.left)
    leaf_nodes(root.right)


# Main program
root = None

n = int(input("Enter number of nodes: "))

for i in range(n):
    data = int(input("Enter value: "))
    root = insert(root, data)

print("\nLevel order traversal:")
level_order(root)

print("\nHeight of BST:", height(root))

print("Leaf nodes:")
leaf_nodes(root)
