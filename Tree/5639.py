import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def add(self, num):
        tmp = self.root
        while True:
            if num < tmp.item:
                if tmp.left is not None:
                    tmp = tmp.left
                else:
                    tmp.left = Node(num)
                    break
            else:
                if tmp.right is not None:
                    tmp = tmp.right
                else:
                    tmp.right = Node(num)
                    break

    def postorder(self):
        self._postorder(self.root)
    
    def _postorder(self, node: Node):
        if node is not None:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.item)
    

r = int(input())
tree = BinaryTree()
tree.root = Node(r)

while True:
    try:
        num = input()
        if not num:
            break
        tree.add(int(num))
    except EOFError:
        break

tree.postorder()