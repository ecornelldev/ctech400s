# Exercise Title: H5P Functions and Variables
---
# Instructional Requirements
## Key Technical Outcome
global vs local
## Exercise Context

## Exercise Instructions

1.
Identify the global and local variables (maybe drag and drop?): 

<pre>
x = 5
y = 7

def add_numbers(a, b):
    r = a + y + b
    return r

add_numbers(1,2)

</pre>

Answer:
local = a, b, r <br>
global = x, y


2. What are the values of `x` and `y` after this program finishes executing (fill in blank)?

<pre>
x = 5
y = 7

def add_values(a, b):
    m = a + b + y
    return m

add_values(x, y)
</pre>

Answer:
y = 7, x = 5


3. What is the value of `m` after this program finishes executing?

<pre>
x = 2
y = 3

def add_values(a, b):
    return a + b + y

m = add_values(x, y)
</pre>

a. 8 # <b>correct answer</b><br>
b. 5 <br>
c. Error <br>
d. None of the above


4. What is the value of `y` after this program finishes executing?

<pre>
x = 2
y = 3

def add_values(a, b):
    y = 5 
    return(a + b + y)

m = add_values(x, y)
y = m+y+x
</pre>

a. 3 <br>
b. 5 <br>
c. 15 # <b> correcr</b> <br>
4. None of the above

5. What is the output of this program?

<pre>
x =  2
y = 3

def add_values(a, b):
    r = 5 
    return(a + b + r)

m = add_values(10, 12)
print(m + ',' + r)

</pre>

a. 27,5 <br>
b. 27 <br>
c. Error <b> # correct </b><br>
d. 22,5 <br>
