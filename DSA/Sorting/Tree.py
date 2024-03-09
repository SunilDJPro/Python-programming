class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def inorder_traversal(root, sorted_list):
    if root:
        inorder_traversal(root.left, sorted_list)
        sorted_list.append(root.value)
        inorder_traversal(root.right, sorted_list)

def tree_sort(arr):
    root = None
    for value in arr:
        root = insert(root, value)
    sorted_list = []
    inorder_traversal(root, sorted_list)
    return sorted_list

# Example usage:
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = tree_sort(arr)
    print("Sorted array:", sorted_arr)
