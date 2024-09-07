class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def traversePreOrder(self):
        print(self.data, end=" ")
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()

    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.data, end=" ")


def print_tree(root, level=0, indent="    "):
    if root is None:
        return
    print_tree(root.right, level + 1, indent)
    print(indent * level + str(root.data))
    print_tree(root.left, level + 1, indent)


root = Node(5)


root.insert(10)
root.insert(11)
root.insert(8)
root.insert(3)
root.insert(4)
root.insert(2)
root.insert(1)

print_tree(root)
root.traversePreOrder()
print()
root.traversePostOrder()
print()
