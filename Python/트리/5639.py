tree = []
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
count = 1
def bst(p, t):
    global tree, count
    if count == len(tree):
        return
    print(count)
    print(t.data, tree[count], p.data)
    if t.data > tree[count]:
        print("left")
        t.left = Node(tree[count])
        t.left.parent = t
        count += 1
        bst(t, t.left)
    if t.data < tree[count] and p.data > tree[count]:
        print("right")
        t.right = Node(tree[count])
        count += 1
        bst(t, t.right)
    return

def postorder(root):
    if root == None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data)
    
    
try:
    while True:
        n = int(input())
        tree.append(n)
except:
    a = Node(tree[0])
    bst(a, a)
    print(a.left.left.right.data)




