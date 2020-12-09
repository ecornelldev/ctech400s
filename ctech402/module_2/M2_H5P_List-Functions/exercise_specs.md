# Exercise Title: H5P List Functions
---
## Key Technical Outcome
Practice with sorted(), reversed(), max(), min(), and sum()

## Exercise Context
Complete the following Questions.

## Exercise Instructions

For the following questions, refer to this list:
<code>a_list = [3, 29, 45, 2, 101, 14]</code>

Q1: Which expression produces the following value?<br>
<pre>a_list = [2, 3, 14, 29, 45, 101]</pre>

  a. list(reverse(a_list)) <br>
  b. sorted(a_list) # <b> correct </b> <br>
  c. min(a_list) <br>
  d. max(a_list) <br>
  e. sum(a_list)

Q2: Which expression produces the following value?<br>
<pre>2</pre>

a. list(reverse(a_list)) <br>
b. sorted(a_list) <br>
c. min(a_list) # <b>correct</b> <br>
d. max(a_list) <br>
e. sum(a_list) <br>

Q3: What is the value of the following expression:<br>
<pre>list(reversed(['dog', 'cat', 'mouse', 'lion', 'zebra', 'bear']))</pre>

a. ['bear', 'zebra', 'lion', 'mouse', 'cat', 'dog']# <b>correct</b><br>
b. ['bear', 'cat', 'dog', 'lion', 'mouse', 'zebra']<br>
c. 'bear'<br>
d. Error<br>

Q4: What is the value of the following expression:<br>
<pre>sorted(['dog', 'cat', 'mouse', 'lion', 'zebra', 'bear'])</pre>

a. ['bear', 'zebra', 'lion', 'mouse', 'cat', 'dog'] <br>
b. 'dog'<br>
c. ['bear', 'cat', 'dog', 'lion', 'mouse', 'zebra'] # <b>correct</b><br>
d. Error<br>

Q5: What is the value of the following expression:<br>
<pre>min(['dog', 'cat', 'mouse', 'lion', 'zebra', 'bear'])</pre>

a. 'dog' <br>
b. 'bear' # <b>correct</b> <br>
c. ['bear', 'cat', 'dog', 'lion', 'mouse', 'zebra']<br>
d. Error<br>

Q6: What is the value of the following expression: <br>
<pre>sum(['dog', 'cat', 'mouse', 'lion', 'zebra', 'bear'])</pre>

a. ['dog', 'cat', 'mouse', 'lion', 'zebra', 'bear']<br>
b. ['bear', 'cat', 'dog', 'lion', 'mouse', 'zebra'] <br>
c. 'dog'<br>
d. Error <b>correct</b> <br>

Q7: What does the following code output when run?<br> 
<pre>a_list = [3, 29, 45, 2, 101, 14]
print(sum(a_list)//len(a_list))</pre>

a. 6 <br>
b. 194 <br>
c. 32 # <b>correct</b> <br>
d. Error

**This isn't quite right, because `/` is exact division. It works if `/` is replaced by `//` or if `2` is removed from the list.**
