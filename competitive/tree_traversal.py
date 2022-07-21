class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, value):
        if value <= self.data:
            if not self.left:
                self.left = Tree(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = Tree(value)
            else:
                self.right.insert(value)

    def contains(self, key):
        if key == self.data:
            return True
        elif key < self.data and self.left:
            return self.left.contains(key)
        elif key > self.data and self.right:
            return self.right.contains(key)
        else:
            return False


# in order traversal left then root then right
def in_order(root):
    if not root:
        return
    in_order(root.left)
    print(root.data)
    in_order(root.right)


# pre order traversal left then root then right
def pre_order(root):
    if not root:
        return
    print(root.data)
    pre_order(root.left)
    pre_order(root.right)


# Post order left -> right -> root
def post_order(root):
    if not root:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.data)


if __name__ == "__main__":
    # # A = Tree("A")
    # B = Tree("B")
    # # C = Tree("C")
    # # B.left = A
    # # B.right = C
    # B.insert("A")
    # B.insert("C")
    # post_order(B)
    # in_order(B)
    root = Tree(10)
    root.insert(5)
    root.insert(15)
    root.insert(8)
    in_order(root)

    print(root.contains(8))
    print(root.contains(12))
