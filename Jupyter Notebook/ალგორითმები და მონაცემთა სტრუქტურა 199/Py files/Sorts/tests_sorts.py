# ტესტირებები (tests)

def test_sort(sort_algorithm):
  # Test 1
  print("Testing:", sort_algorithm.__doc__)
  print("Testcase #1: ", end='')
  
  A = [4, 2, 5, 1, 3]
  A_sorted = [1, 2, 3, 4, 5]
  
  sort_algorithm(A)
  
  print("OK!" if A == A_sorted else "Fail!")


  # ==========================
  # Test 2
  print("Testcase #2: ", end='')
  
  A = list(range(10, 20)) + list(range(1, 10))
  A_sorted = list(range(1, 20))
  
  sort_algorithm(A)
  
  print("OK!" if A == A_sorted else "Fail!")


  # ==========================
  # Test 3
  print("Testcase #3: ", end='')
  
  A = [4, 2, 4, 2, 1]
  A_sorted = [1, 2, 2, 4, 4]
  
  sort_algorithm(A)
  
  print("OK!" if A == A_sorted else "Fail!")
