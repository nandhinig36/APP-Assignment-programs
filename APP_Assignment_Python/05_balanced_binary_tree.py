class Node:
    def __init__(self, value, left=None, right=None):
        self.value, self.left, self.right = value, left, right

def is_balanced(root):
    def height(node):
        if node is None: return 0
        left, right = height(node.left), height(node.right)
        if left == -1 or right == -1 or abs(left-right) > 1: return -1
        return 1 + max(left, right)
    return height(root) != -1

if __name__ == "__main__":
    root = Node(3, Node(9), Node(20, Node(15), Node(7)))
    print("Balanced:", is_balanced(root))
