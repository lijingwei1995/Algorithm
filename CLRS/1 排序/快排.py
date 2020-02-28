def QUICK_SORT(A, L, R):
    # 递归边界
    # 每次处理包含从左下标到右下标所包含的数组
    # 若左下标大于右下标表示数组为空，返回
    # 若左下标等于右下标表示数组长度为1，不需要处理，返回
    if L < R:
    
        # 划分
        # 选取最后一个数作为主元（保持左侧稳定）
        x = A[R]
        
        i = L
        while i <= R-1: # 刨去主元
            if A[i] > x: # 如果是 >= 可能会导致不稳定
                # 寻找 j
                j = i + 1
                while j <= R-1:
                    if A[j] <= x:
                        # 交换
                        temp = A[i]
                        A[i] = A[j]
                        A[j] = temp
                        continue
                    else:
                        j += 1
                # j 超范围，break
                if j == R:
                    break
            else:
                i += 1
        # 主元与A[i]交换
        temp = A[i]
        A[i] = A[R]
        A[R] = temp
        
        # 分治
        QUICK_SORT(A, L, i-1)
        QUICK_SORT(A, i+1, R)
        
    return A

A = [2,5,3,8,5,1,0]
QUICK_SORT(A, 0, len(A)-1)