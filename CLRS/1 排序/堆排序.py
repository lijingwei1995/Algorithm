# 最大堆的heapify
# 这是一个递归函数，他可以调整 任意左右子树以满足性质，但父节点未知的树
def MAX_HEAPIFY(A, heap_size, i):
    # 下标i如果是父节点
    left  = 2 * i + 1
    right = 2 * i + 2
    # 找到最大节点
    max = i
    if left  < heap_size and A[left]  > A[i]  : max = left  # 将数字比较写在左边可以避免超限问题
    if right < heap_size and A[right] > A[max]: max = right
    # 如果最大不是i，则与最大的交换，并继续递归该分支
    if max != i:
        temp = A[i]
        A[i] = A[max]
        A[max] = temp
        MAX_HEAPIFY(A, heap_size, max)

# 建堆
def BUILD_MAX_HEAP(A):
    # 从最底下的一个父节点至顶，以此执行MAX_HEAPIFY
    first_parent = int(len(A)/2) - 1
    for i in range(first_parent, -1, -1):
        MAX_HEAPIFY(A, len(A), i)

# 堆排序
# 我们可以将最大的数拿出，将最后一个数字重新放回堆，然后执行HEAPIFY
def HEAP_SORT(A):
    # 先建堆
    BUILD_MAX_HEAP(A)
    
    # 依次执行交换、HEAPIFY
    heap_size = len(A)
    while heap_size > 0:
        temp = A[0]
        A[0] = A[heap_size-1]
        A[heap_size-1] = temp
        
        MAX_HEAPIFY(A, heap_size, 0)
        
        heap_size -= 1

A = [16, 3, 10, 8, 1, 9, 14, 2, 4, 7]
HEAP_SORT(A)
A