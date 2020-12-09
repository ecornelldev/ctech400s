# Exercise Title:
---
# Instructional Requirements
## Key Technical Outcome

## Exercise Context

List methods vs functions

reversed() vs .reverse()

The reversed() function does not modify the list it operates on, but instead returns a <b>new</b> list with the same elements in reversed order. It does not have an <i>effect</i> on the original list, but it does return a <i>value</i>.

The .reverse() method modifies the list it operates on. It does not return a useful </i>value</i> (it returns `None`), but it does have an <i>effect</i> on the list.

## Exercise Instructions

<b>Question 1:</b><br>
<code>a_list = ['Paul', 'George', 'Ringo', 'John']</code> <br>
What is the value of <code>a_list</code> after <code>list(reversed(a_list))</code>? <br>

a. a_list = ['Paul', 'George', 'Ringo', 'John'] # <b>correct</b><br>
b. a_list = ['John', 'Ringo', 'George', 'Paul'] <br>
c. a_list = ['George', 'John', 'Paul', 'Ringo'] <br>
d. a_list = ['John', 'George', 'Ringo', 'Paul']

Display after answer is revealed: Function reversed(a_list) leaves a_list unmodified and returns a new list with the same elements in reversed order.

<b>Question 2:</b><br>
<code>num_list = [2, 10, 7, 35, 6]</code> <br>
What is the value of <code>num_list</code> after <code>num_list.reverse()</code>? <br>

a. num_list = [2, 10, 7, 35, 6] <br>
b. num_list = [6, 35, 7, 10, 2] # <b> correct </b> <br>
c. num_list = [2, 6, 7, 10, 35]<br>
d. num_list = [6, 10, 7, 35, 2]

Display after answer is revealed: The reverse() method modifies num_list. It does not return anything (None), but changes the num_list itself.

<b>Question 3:</b><br>
<code>a_list = [1, 2, 3, 4 ,5]</code> <br>
If you want to change the value of a_list to be equal to [5,4,3,2,1], which function should you use?<br>

a. list(reversed(a_list)) <br>
b. a_list.reversed() # <b> correct </b> <br>
c. sorted(a_list) <br>
d. reversed(a_list)

Display after answer is revealed: You should use the reverse() method because it modifies the list it operates on.



## Environment/s Used
Terminal. Python interpreter
