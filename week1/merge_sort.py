def sort(l: list):
    '''
    Function to merge-sort an input array
    '''
    n = len(l)
    if n == 1:
        return l
    else:
        mid = n//2
        left = sort(l[ :mid])
        right = sort(l[mid: ])

    i = 0
    j = 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i = i+1
        else:
            merged.append(right[j])
            j = j+1
    merged += left[i: ]
    merged += right[j: ]
    return merged


def sort_nd(l: list, d: int):
    '''
        N-dimentional merge-sort
        l: input list
        n: dimention to sort by
        '''
    n = len(l)
    if n==1:
        return l
    else:
        mid = n//2
        left = sort_nd(l[ :mid], d)
        right = sort_nd(l[mid: ], d)
    
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i][d] < right[j][d]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j+=1
    result += left[i:]
    result += right[j:]

return result