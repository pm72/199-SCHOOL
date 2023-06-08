from tests_sorts import test_sort
from sorts import bubble_sort, inseretion_sort, selection_sort


if __name__ == '__main__':
  test_sort(bubble_sort)
  print()
  
  test_sort(inseretion_sort)
  print()
  
  test_sort(selection_sort)
  print()

  input("\n\nDone!..\n")
