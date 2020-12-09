# Exercise Title: H5P References
---
## Key Technical Outcome

## Exercise Context
Th exercise below will test your comprehension of the difference between methods and functions and the effects they can have on the values of variables.

## Exercise Instructions

Question 1: 
We want to sort `a_list` but do not want to change the value of `a_list`. Rather, we want the sorted result to be saved to the variable `sorted_a_list`. How do we accomplish this?
<code>a_list = [12,20,18,14,20]</code> 

a. a_list.sort() <br>
b. sorted_list.sort() <br>
c. sorted_list = a_list.sort() <br>
d. sorted_list = sorted(a_list) <b>#correct</b><br>

Question 2: 
Examine the following block of code:
<pre>a_list = [1,2,3,4,5]
b_list = a_list
a_list.reverse()</pre>

After this code executes, what is the value of `b_list`?

a. None <br>
b. [1,2,3,4,5] <br>
c. [5,4,3,2,1] # <b>correct</b><br>
d. [5,2,3,4,1]

What is the value of `a_list`?

a. None <br>
b. [1,2,3,4,5]<br>
c. [5,4,3,2,1] # <b>correct</b><br>
d. [5,2,3,4,1]

Question 3: <br>
Examine the following block of code:<br>
<pre>a_list = [1,2,3,4,5]
b_list = a_list
list(reversed(a_list))</pre>
After this code executes, what is the value of `b_list`?

a. None <br>
b. [1,2,3,4,5] # <b>correct</b> <br>
c. [5,4,3,2,1] <br>
d. [5,2,3,4,1]

What is the value of a_list?

a. None <br>
b. [1,2,3,4,5] # <b>correct</b><br>
c. [5,4,3,2,1] <br>
d. [5,2,3,4,1]

Question 4: <br>
Examine the following block of code:<br>
<pre>a_list = [1,2,3,4,5]
b_list = list(reversed(a_list))</pre>
After this code executes, what is the value of `b_list`?

a. None <br>
b. [1,2,3,4,5]  <br>
c. [5,4,3,2,1] # <b>correct</b> <br>
d. [5,2,3,4,1]

What is the value of a_list?

a. None <br>
b. [1,2,3,4,5] # <b>correct</b><br>
c. [5,4,3,2,1] <br>
d. [5,2,3,4,1]

Question 5:<br>
Examine the following block of code:<br>
<pre>a_list = [1,2,3,4,5]
b_list = a_list.reverse()</pre>

After this code executes, what is the value of `b_list`?

a. None # <b>correct</b><br>
b. [1,2,3,4,5]  <br>
c. [5,4,3,2,1]  <br>
d. [5,2,3,4,1]

What is the value of a_list?

a. None <br>
b. [1,2,3,4,5] <br>
c. [5,4,3,2,1] # <b>correct</b><br>
d. [5,2,3,4,1]
