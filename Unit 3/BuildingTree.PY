class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

root = node(8)
print(root.data)
root.left = node(9)        #root.left is an object
print(root.left.data)
root.right = node(10)
print(root.right.data)
print(root.right.left)