#correct

def solution(A):
    right = sorted([k + v for k, v in enumerate(A)])
    left = sorted([k - v for k, v in enumerate(A)])

    j = 0
    counter = 0
    for i, v in enumerate(right):
        while j < len(right) and v >= left[j]:
            counter += j - i
            j += 1
        if counter > 10000000:
            return -1
    return counter


#correct, but not for too big values

def solution(A):
    plane = []
    for i in range(len(A)):
        plane.append(set(range(i-A[i],i+A[i]+1)))

    count = 0
    for i in range(len(plane)):
        for k in range(i+1, len(plane)):
             if plane[i].intersection(plane[k]):
                count += 1
                if count > 10000000:
                    return -1

    return count

# print(solution([1,5,2,1,4,0]))