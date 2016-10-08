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
