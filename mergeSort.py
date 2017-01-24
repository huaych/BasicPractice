# mergeSort(L) sorts the elements in L in ascending order
def mergeSort(L):
    if len(L) < 2:
        return L
    else:
        middle = int(len(L) / 2)
        left = L[:middle]
        right = L[middle:]
        left_sort = mergeSort(left)
        right_sort = mergeSort(right)
        return merge(left_sort, right_sort)
        
def merge(left,right):
    i = 0
    j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i == len(left):
        result = result + right[j:]
    elif j == len(right):
        result = result + left[i:]
    return result
            
