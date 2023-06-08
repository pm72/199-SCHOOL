# SORTS

# სორტირება ბუშტებით (bubble sort)
def bubble_sort(A):
  '''Bubble sort'''
  
  N = len(A)
  
  for j in range(N-1, 0, -1):
    for i in range(j):
      if A[i] > A[i+1]:
        A[i], A[i+1] = A[i+1], A[i]
  
  
# სორტირება ჩასმით (insertion sort)
def inseretion_sort(A):
  '''Insertion sort'''
  ...


# სორტირება ამორჩევით (selection sort)
def selection_sort(A):
  '''Selection sort'''
  ...
