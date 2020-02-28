import LinkedList

def printList(listNode):
    r = []
    while listNode:
        r.append(listNode.val)
        listNode = listNode.next
    
    return r

def deleteDuplication(pHead):
    head = LinkedList.ListNode()
    head.next = pHead
    # 以后使用p代表前一个节点,q代表后一个节点
    # 当只需要一个节点操作，如遍历时，使用p
    # 当需要执行诸如删除操作时，使用p和q，删除q所指的节点就是讲p.next置为q.next
    p = head
    q = pHead
    
    # 遍历中，判断q是否为None即可
    # 由于这里需要比较q.next，所以判断q.next是否None即可
    while q.next: #r
        if q.val != q.next.val:
            if q != p.next:
                p.next = q.next
            else:
                p = q
            
        q = q.next

    # 判断链表结尾是重复的问题
    if q != p.next:
        p.next = q.next
    
    return head.next

l = LinkedList.LinkedList([1,1,1,1,2])
pHead = deleteDuplication(l.root)
print(printList(pHead))