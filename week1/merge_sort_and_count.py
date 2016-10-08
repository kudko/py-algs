def sort_and_count(l: list):
    '''
    Function to merge-sort an input array
    and calculate the number of inversions 
    '''
    n = len(l)
    if n == 1:
        return [0, l]
    else:
        mid=n//2
        [inv_left, left] = sort_and_count(l[ :mid])
        [inv_right, right] = sort_and_count(l[mid: ])

    i = 0
    j = 0
    merged = []
    inv_merged = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inv_merged += len(left[i: ])
            j += 1
    merged += left[i: ]
    merged += right[j: ]
    
    return [inv_left + inv_right + inv_merged, merged] 
