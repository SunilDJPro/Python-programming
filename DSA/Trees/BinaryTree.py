class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None

    #        1
    #     2    3
    #    4 5  6 7
    #   8


# Example usage:
if __name__ == "__main__":
    # Creating a binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(8)

    # Traversing the binary tree (pre-order traversal)
    def preorder_traversal(node):
        if node:
            print(node.value, end=" ")
            preorder_traversal(node.left)
            preorder_traversal(node.right)

    print("Pre-order traversal:", end=" ")
    preorder_traversal(root)
