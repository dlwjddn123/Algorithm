class Node:
    def __init__(self,data, left, right):
        self.data = data
        self.left = left
        self.right = right
N = int(input())   
root = {}

for _ in range(N):
    data, left, right = map(str, input().split())
    root[data] = Node(data, left, right)

def preorder(data):
    if data =='.':
        return
    print(data, end="")
    preorder(root[data].left)
    preorder(root[data].right)

def inorder(data):
    if data == '.':
        return
    inorder(root[data].left)
    print(data, end="")
    inorder(root[data].right)

def postorder(data):
    if data == '.':
        return
    postorder(root[data].left)
    postorder(root[data].right)
    print(data, end="")

preorder("A")
print()
inorder('A')
print()
postorder("A")