import LinkedList

def printList(listNode):
    r = []
    while listNode:
        r.append(listNode.val)
        listNode = listNode.next
    
    return r

def ReverseList(pHead):
    
    if not pHead:
        return None
    
    if not pHead.next:
        return pHead
    
    p = pHead
    q = p.next
    
    while q:
        r = q.next
        p.next = None
        q.next = p
        p = q
        q = r
    
    return p

l = LinkedList.LinkedList([4, 1, 2, 3, 8])
h = ReverseList(l.root)
print(h.next.next.val)