class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


        #    5
        #  2   6
    #    1  3 4 7



class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)
        #Ignore duplicates (values already exist in the tree)

    def inorder_traversal(self):
        def _inorder_traversal_recursive(node):
            if node:
                _inorder_traversal_recursive(node.left)
                print(node.value, end=" ")
                _inorder_traversal_recursive(node.right)

        _inorder_traversal_recursive(self.root)



if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(550)
    bst.insert(380)
    bst.insert(720)
    bst.insert(550)
    bst.insert(205)
    bst.insert(470)
    bst.insert(640)
    bst.insert(890)

    print("In-order traversal:")
    bst.inorder_traversal()
 