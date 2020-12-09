# Exercise Title: H5P Strings are Immutable
---
## Key Technical Outcome

## Exercise Context
Lists are mutable - list methods change the orignal list<br>
Strings are immutable - string methods do NOT change the orignal string.<br>
Therefore, some of the methods we have used on lists, such as .append(), cannot be used on strings. <br>
If you attempt to use such a method, you will receive an error. <br>
One way to make a change to a string is to create a new string that contains the desired change.<br>


## Exercise Instructions

### Question 1:
<pre>
my_string = 'Yellow Submarine.'<br>
s = my_string.replace('Y', 'F')
</pre>

What is the value of <code>my_string</code>?<br>
'Yellow Submarine.' # <b> correct </b> <br>
'Fellow Submarine.' <br>
None of the above <br>

What is the value of <code>s</code>?
'Yellow Submarine.' <br>
'Fellow Submarine.' # <b> correct </b> <br>
None of the above <br>

### Question 2
<pre>
my_string = 'Flood'<br>
s = my_string.replace('F', 'G').replace('l', '') + ' ' + 'Bye!'<br>
</pre>
What is the value of s? # <b> Free text Quiz: 'Good Bye!' </b>
 
### Question 3
which will the following operation work on? <br>

<code>variable_name.append('s') </code>

a. list #<b> correct </b> <br>
b. string
c. both
d. neither

### Question 4
We want to add on to string <code>s = 'Hello</code> to form the phrase 'Hello there!'<br>
Which of the following will work? (select all that apply)

a. s = s + ' there!'  # <b> correct </b><br> 

b. s.append(' there!') <br>

c. s= s + ' ' + 'there!' # <b> correct </b> <br>

d. r = ' there!' <br>
  s.extend(r) <br>

e. r = ' there!' <br>
  s.append(r)
