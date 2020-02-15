from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, seq = None):
        def createTree(index):
            if not seq or index >= len(seq) or seq[index] is None:
                return None
            else:
                n = TreeNode(seq[index])
                n.left  = createTree(2 * index + 1)
                n.right = createTree(2 * index + 2)
                return n

        self.root = createTree(0)
    
    # 前序遍历
    def DLR(self):
        def DLR_node(node):
            r = [] # result
            r.append(node.val)
            if node.left is not None:
                r += DLR_node(node.left)
            if node.right is not None:
                r += DLR_node(node.right)
            return r
        
        return DLR_node(self.root)

    # 中序遍历
    def LDR(self):
        def LDR_node(node):
            r = [] # result
            if node.left is not None:
                r += LDR_node(node.left)
            r.append(node.val)
            if node.right is not None:
                r += LDR_node(node.right)
            return r
        
        return LDR_node(self.root)

    # 后序遍历
    def LRD(self):
        def LRD_node(node):
            r = [] # result
            if node.left is not None:
                r += LRD_node(node.left)
            if node.right is not None:
                r += LRD_node(node.right)
            r.append(node.val)
            return r
        
        return LRD_node(self.root)

    # 广度优先遍历
    def BFS(self):
        q = deque()
        r = []

        q.append(self.root)
        while q:
            node = q.popleft()
            r.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return r

    # 搜索节点，使用广度优先搜索
    def search(self, val):
        q = deque()
        q.append(self.root)
        while q:
            node = q.popleft()
            if node.val == val:
                return node
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return None    

# t = BinaryTree("ABCDEF")
# t = BinaryTree([3,5,1,6,2,0,8,None,None,7,4])

# print(t.DLR())
# print(t.LDR())
# print(t.LRD())
# print(t.BFS())
# print(t.search("s"))