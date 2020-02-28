def MERGE_SORT(A):
    # 这是一个递归算法，分为3个步骤
    L = len(A)
    
    # 递归边界
    if L == 1:
        return A
    
    # 分解，将数组一分为二
    # 每一个部分都递归调用本函数
    A1 = MERGE_SORT(A[:int(L/2)])
    A2 = MERGE_SORT(A[int(L/2):L])
    
    # 合并
    # 归并算法，交互的更改哨兵，另一数组的小于哨兵的值都依次被添加
    r = []
    i, j = 0, 0
    A1.append(float("inf"))
    A2.append(float("inf"))
    while i + j < len(A1) + len(A2):
        if A1[i] < A2[j]:
            r.append(A1[i])
            i += 1
        else:
            r.append(A2[j])
            j += 1
    return r
   
MERGE_SORT([2,5,3,8,5,1,0])