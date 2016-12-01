A = [99, 11, 11, 11, 77, 22]
B = [10, 30, 40, 30, 80, 30]

def bubbleSort(A):
    for k in range(1,len(A)):
        for i in range(0,len(A) - k):
            if A[i] > A[i+1]:
                   A[i],A[i+1] = A[i+1],A[i]

print(A,B, sep = '\n')                   

AB = list(zip(B,A))
bubbleSort(AB)
AB = AB[::-1]

for i in range(len(AB) - 1):
    if AB[i][0] == AB[i + 1][0] and AB[i][1] > AB[i + 1][1]:
        AB[i],AB[i + 1] = AB[i + 1],AB[i]

for i in range(len(AB)):
    A[i] = AB[i][0]
    B[i] = AB[i][1]
    
print(A,B, sep = '\n')

'''AB = [list(x) for x in zip(*sorted(zip(A,B), key=lambda pair: pair[1]))]
A = AB[0]
A = A[::-1]
B = AB[1]
B = B[::-1]'''
