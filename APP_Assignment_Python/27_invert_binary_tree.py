class Node:
    def __init__(self, value, left=None, right=None):
        self.value, self.left, self.right = value, left, right

def invert(root):
    if root:
        root.left, root.right = invert(root.right), invert(root.left)
    return root

def preorder(root):
    return [] if root is None else [root.value] + preorder(root.left) + preorder(root.right)

if __name__ == "__main__":
    root = Node(4, Node(2, Node(1), Node(3)), Node(7, Node(6), Node(9)))
    invert(root)
    print("Inverted tree preorder:", preorder(root))
