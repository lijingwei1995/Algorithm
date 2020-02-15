class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self, seq = None):
        if seq[0]:
            self.root = ListNode(seq[0])
            node = self.root

        for index in range(1, len(seq)):
            node.next =  ListNode(seq[index])
            node = node.next

    def getList(self):
        r = []
        node = self.root
        while node:
            r.append(node.val)
            node = node.next
        
        return r

# l = LinkedList([1, 7, 9, 5])
# print(l.getList())