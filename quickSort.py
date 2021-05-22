# Quicksort
def quickSort(A,p,r):
    if p < r:
        q = partition(A,p,r)
        quickSort(A,p,q-1)
        quickSort(A,q+1,r)
    
def partition(A,p,r):
    pivot = A[r]
    smaller = p 
    for j in range(p,r):
        if A[j] <= pivot:
            A[smaller], A[j] = A[j], A[smaller]
            smaller = smaller + 1          
    A[smaller], A[r] = A[r], A[smaller]
    return smaller
    
# Read file and save numbers to variable
text_file = open("dane.txt", "r")
lines = text_file.read().split('\n')
text_file.close()
for i in range(0, len(lines)):
    lines[i] = int(lines[i])

# Sort
quickSort(lines, 0, len(lines)-1)