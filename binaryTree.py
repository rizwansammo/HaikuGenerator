class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.value, end=" ")
        in_order_traversal(root.right)

# Example usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
in_order_traversal(root)  # Output: 4 2 5 1 3
