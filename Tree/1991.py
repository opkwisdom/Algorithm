class Node:
    def __init__(self, root, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right

    def update_node(self, root, left, right):
        stack = [self]
        while stack:
            tmp = stack.pop()
            if tmp.root == root:
                tmp.left = None if left == '.' else Node(left)
                tmp.right = None if right == '.' else Node(right)
                break
            if tmp.right:
                stack.append(tmp.right)
            if tmp.left:
                stack.append(tmp.left)
    
    def preorder(self):
        print(self.root, end='')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.root, end='')
        if self.right:
            self.right.inorder()
    
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.root, end='')

tree = Node('A')

N = int(input())
for _ in range(N):
    root, left, right = list(input().strip().split())
    tree.update_node(root, left, right)

tree.preorder()
print()
tree.inorder()
print()
tree.postorder()
print()