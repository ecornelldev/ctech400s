# Exercise Title: Useful List Methods
---
## Key Technical Outcome
Give a list of unsorted numbers and ask students to remove the largest number from the list.

Two ways to accomplish this:
1. Use max() to get the largest value and remove() to remove that value 
2. Use sort() to sort the list and pop() to remove last element()

**Only method 1 works, because method 2 destructively alters the list. They could use int_list.remove(reverse(sorted(int_list))[0]). But max() is much better.**

## Exercise Context
Examine the code in <code>exercise.py</code> in the code editor. It contains an unsorted list of integers <code>int_list</code>.

int_list = [97, 85, 45, 67, 2, 101, 9, 36, 4]

## Exercise Instructions
Using some of the list methods and functions you have learned, find a way to remove the largest integer from the list.

Note: At the end of your program, <code>int_list</code> should have the value  [97, 85, 45, 67, 2, 9, 36, 4].
 
 
## Any Unique Requirements or Notes?

---
# Technical Requirements
<em><strong></strong></em>

## Environment/s Used
Terminal. Python interpreter. Code editor

## Language/s Used
<em></em>

## Package/s Required
<em>Python 3</em>
