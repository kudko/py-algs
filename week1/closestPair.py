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



def closest_pair(P: list):
    '''
    Take a list of points as an input
    Use divide&conquer to find two closest points
    Complexity: O(nlogn)
    '''
    # Sort points by x-coordinate
    Px = sort_nd(P, 0)
    Py = sort_nd(P, 1)

    # Invoke a recursive divide&conquer algorithm for the closest pair
    # Return only the pair of points, since distance is not computed here
    return _closest_pair(Px, Py)[1]

def _closest_pair(Px, Py):
    '''
    Takes two lists of SORTED by X and by Y corrdinates points and
    find two closest points by divide&conquer approach 
    '''
    n = len(Px)
    
    if n < 2:
        return [float("inf"), (None, None)]
    else:
        Lx = Px[ :n//2] # Left half of Px
        Rx = Px[n//2: ] # Right half of Px
        median = Lx[-1][0] # the most extreme x coordinate in our left half
        
        # Instead of resorting Lx and Rx by Y-coordinate, we can save some
        # time and achieve the same result by simply taking an already sorted
        # list P by Y-coordinate (Py) and subsampling those poins whose
        # X-coordinates lie on the left (Ly) or on the right (Ry) from the median
        Ly = [p for p in Py if p[0] <= median]
        Ry = [p for p in Py if p[0] > median]

        # Recursively invoke _closest_pair for the Left and Right halves of P
        [delta1, pair1] = _closest_pair(Lx, Ly)
        [delta2, pair2] = _closest_pair(Rx, Ry)

        # If min distance is in any half pair
        # Initialize the starting point
        [delta, pair_min] = [delta1, pair1]
        if delta < delta1:        
            [delta, pair_min] = [delta2, pair2]

        # If min distance is in split pair
        # Using list comprehensions, find an Sy subset of sorted by
        # Y-coordinate points that are no more than delta away from
        # the median X-coordinate
        Sy = [p for p in Py if p[0]>median-delta and p[0]<median+delta]
        n_Sy = len(Sy)
        
       # Start walking up through Sy
        for i, p1_Sy in enumerate(Sy[ :-1]):
            # For every y in Sy we only have to consider 7 closest points 
            for j, p2_Sy in enumerate(Sy[i+1 : i+8 if i+8<n_Sy else n_Sy]):
                if p2_Sy[1]-p1_Sy[1] < delta:
                    # If we found a closer pair, update the result 
                    [delta, pair_min] = [p2_Sy[1]-p1_Sy[1], [p1_Sy, p2_Sy]]
        '''Alternative
        for i in range(len(Sy[ :-1])):
            k=i+1
            while k<n_Sy and Sy[k][1]-Sy[i][1]<d_min:
                if Sy[k][1]-Sy[i][1]<closest:
                    [closest, closest_pair] = [Sy[k][1]-Sy[i][1], [Sy[k],Sy[i]]]
                k += 1
        '''
        return [delta, pair_min]
        


import math
def closest_pair_brute(P: list):
    '''
    Take a list of points as an input
    Use brute force method to calculate a distance between
    every pair of points in the list, exclusing self-pairs
    Complexity: O(n^2)
    '''
    if len(P)<2:
        # If there are less then two points, the distance is infinity
        return float("inf"), (None, None)
    else:
        # Find starting distance between p1 and p2
        min_dist = math.sqrt((P[1][0]-P[0][0])**2 + (P[1][1]-P[0][1])**2)
        # Define starting pair of points that has min distance
        min_pair = [P[0], P[1]]

        # Iterate through all the points in a triangular manner  
        for i, p1 in enumerate(P[ :-1]):
            for j, p2 in enumerate(P[i+1: ]):
                # For each pair calculate distance 
                d = math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)
                # Check whether this distance is smaller than min distance
                if d < min_dist:
                    # If we found a smaller distance
                    # Update min distance and a pair of corresponding points 
                    min_dist = d
                    min_pair = [p1, p2]

        # Return the result as a list of [min dist and min pair of points]
        return [min_dist, min_pair]



L=[(0,0),(7,6),(2,20),(12,5),(16,16),(5,8),\
	 (19,7),(14,22),(8,19),(7,29),(10,11),(1,13),(11,1)]

print(closest_pair(L))
print(closest_pair_brute(L))

