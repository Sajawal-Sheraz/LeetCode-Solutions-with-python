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

    def search(self, node, target):
        if node is None or node.data == target:
            return node
        if target < node.data:
            return self.search(node.left, target)
        else:
            return self.search(node.right, target)


root = Node(10)
root.insert(5)
root.insert(15)
root.insert(3)
root.insert(7)

result = root.search(root, 7)
if result:
    print("value is present in Tree")
else:
    print("value is not present in Tree")

    #         10
    #        /  \
    #       5    15
    #     /   \
    #    3     7


# Time Complexity:

# Insertion: O(log n) on average, O(n) in the worst case (when the tree becomes unbalanced).
# Search: O(log n) on average, O(n) in the worst case (when the tree becomes unbalanced).


# Space Complexity:
# The space complexity of the BST depends on the number of nodes in the tree and the height of the tree.
# In the worst case, when the tree is completely unbalanced (resembling a linked list), the space complexity is O(n).
# In the average case, when the tree is balanced, the space complexity is O(log n).
