class TreeNode:
    def __init__(self, val=None):
        self.value = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def isempty(self):
        return self.root is None

    def insert(self, data):
        if self.isempty():
            self.root = TreeNode(data)
            print("Inserted successfully")
        else:
            current = self.root
            while True:
                if data < current.value:
                    if current.left is None:
                        current.left = TreeNode(data)
                        print("Inserted successfully")
                        break
                    else:
                        current = current.left
                elif data > current.value:
                    if current.right is None:
                        current.right = TreeNode(data)
                        print("Inserted successfully")
                        break
                    else:
                        current = current.right
                else:
                    break

    def inorder(self):
        if self.isempty():
            return
        stack = []
        current = self.root
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                print(current.value, end=" ")
                current = current.right
            else:
                break

    def preorder(self):
        if self.isempty():
            return
        stack = [self.root]
        while stack:
            current = stack.pop()
            print(current.value, end=" ")
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

    def postorder(self):
        if self.isempty():
            return
        stack = []
        current = self.root
        last_visited = None
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                peek = stack[-1]
                if peek.right and last_visited != peek.right:
                    current = peek.right
                else:
                    print(peek.value, end=" ")
                    last_visited = stack.pop()

    def levelorder(self):
        if self.isempty():
            return
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            print(current.value, end=" ")
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

bt = BinaryTree()
bt.insert(15)
bt.insert(10)
bt.insert(18)
bt.insert(4)
bt.insert(11)
bt.insert(16)
bt.insert(20)
bt.insert(13)

print("Inorder Traversal:")
bt.inorder()
print("\nPreorder Traversal:")
bt.preorder()
print("\nPostorder Traversal:")
bt.postorder()
print("\nLevelorder Traversal:")
bt.levelorder()
