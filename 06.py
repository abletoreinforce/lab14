A = [3,5,7]

def bubble_swapcount(A):
    swapcount = 0
    for k in range(1,len(A)):
        for i in range(0,len(A) - k):
            if A[i] > A[i+1]:
                swapcount += 1
                A[i],A[i+1] = A[i+1],A[i]

    return swapcount

print(bubble_swapcount(A))
