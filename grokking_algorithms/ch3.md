# Chapter 3: Recursion

## Base case and recursive case

- every recursive function has two parts:
  - *base case*: when the function doesn't call itself
  - *recursive case*: when the function calls itself

## The stack

- *push*: add new item to top of stack
- *pop*: remove topmost item (last item added)

### The call stack

- each time a function is called, it's added to the top of the call stack (incl. function params)
- each time a function returns (i.e., most recent function), that function is popped off the call stack

### The call stack with recursion

- recursive calls just add calls to the same function to the call stack
- potentially cleaner code, but more memory intensive than a loop

## Exercises

1. `greet(name=Maggie)` was the first call and `greet2(name=Maggie)` was the second call. `greet()` has not yet returned when `greet2()` was called and will return after `greet2()` finishes.
2. it keeps adding calls to the recursive function until it runs out of memory (stack overflow haha)