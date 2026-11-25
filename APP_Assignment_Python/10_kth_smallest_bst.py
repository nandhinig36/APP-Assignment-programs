class Node:
    def __init__(self, value, left=None, right=None):
        self.value, self.left, self.right = value, left, right

def kth_smallest(root, k):
    stack, node = [], root
    while stack or node:
        while node:
            stack.append(node); node = node.left
        node = stack.pop()
        k -= 1
        if k == 0: return node.value
        node = node.right
    raise ValueError("k exceeds number of nodes")

if __name__ == "__main__":
    root = Node(8, Node(3, Node(1), Node(6, Node(4), Node(7))), Node(10, None, Node(14, Node(13))))
    k = int(input("k: "))
    print("Kth smallest:", kth_smallest(root, k))
