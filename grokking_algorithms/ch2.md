# Chapter 2: Selection Sort

## Arrays and Linked Lists

- run times:
  - arrays: O(1) read, O(n) insert, O(n) delete
  - linked lists: O(n) read, O(1) insert, O(1) delete

## Selection Sort

- algorithm:
  - find highest (or lowest) value in list
  - append to new list
  - remove value from old list (or skip)
  - repeat until all items have been migrated to new list
- run time: O(n^2)
- code: `./code/selection_sort.py`

## Exercises

1. linked list - many inserts + few reads
2. linked list - quick insert, always reading first element
3. array - quick access
4. 
   1. array for inserts - O(n) complexity
   2. you need to expand the array frequently
5. faster for search than a linked list, but slower search than array (i.e., can't do binary search since it's not sorted)
6. 