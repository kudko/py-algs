def quick_sort(L: list, pivot: chr):
    '''
    Quick Sort based with a pivot selection procedure
    pivot:  f: first element 
            m: median element 
            l: last element
    '''
    if len(L)<=1:
        return L
    else:
        left, mid, right = [], [], []
        # Choosing pivot
        if pivot == "f":
            p_i = 0 # pivot is first element
        elif pivot == "m":
            p_i = choosing_pivot(L) # pivot is median 
        elif pivot == "l":
            p_i = len(L)-1 # pivot is last element
        pvt = L[p_i]
       
        for x in L:
            if x < pvt:
                left.append(x)
            if x == pvt:
                mid.append(x)
            if x > pvt:
                right.append(x)
        
        res1 = quick_sort(left, pivot)
        res2 = quick_sort(right, pivot)
        return res1 + mid + res2

def choosing_pivot(A):
    if len(A)%2 == 0:
        middle = len(A)//2-1
    else:
        middle = len(A)//2
    return (median(A, 0, middle, len(A)-1))


def median(inputArray, a, b, c):
	if ( inputArray[a] > inputArray[b] ):
		if ( inputArray[a] > inputArray[c] ):
			if (inputArray[b] > inputArray[c]):
				return b
			else:
			    return c
		else:
		    return a
	else:
		if ( inputArray[b] > inputArray[c] ):
			if (inputArray[a] > inputArray[c]):
				return a
			else:
			    return c
		else:
		    return b


lst=[1,5,3,6,9,8,2,0,6,10,4]
print(quick_sort(lst, "m"))



