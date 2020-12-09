# Exercise Title:
---
# Instructional Requirements
## Key Technical Outcome
mutability and immutability
strings vs lists.
## Exercise Context
[perhaps explain immutable vs mutable and references here OR add explanations to each MC question to further explain mutability and scope]

## Exercise Instructions

What is the value of <code>a</code> after this program finishes executing? (free text answer)

<pre>
def multiple_strings(s):
    s = s*5
    return s

a =  'foo'
b = multiple_strings(a)
</pre>
Answer: 'foo'

What is the value of <code>a</code> after this program finishes executing?

<pre>
def multiply_lists(l):
    l = l*5
    return l

a =  [1,2,3]
b = multiply_lists(a)
</pre>

a. [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]<br>
b. [1, 2, 3] <b> # correct </b></br>
c. [5, 10, 15] <br>
d. ERROR


What is the value of <code>a</code> after this program finishes executing?

<pre>
def add_to_list(l):
    l.append(5)
    return l

a =  [4,5,6]
b = add_to_list(a)
</pre>

a. [4,5,6]<br>
b. [5,4,5,6] <br> 
c. [4,5,6,5]<b> # correct </b> <br>
d. ERROR

Display after answer is revealed: Lists are mutable. A list's value can change. Variables store references to lists. Therefore, a local variable inside a function and a global variable outside the function can refer to the same list. An operation (such as method append()) that modifies a list that is applied to the local variable in a function will therefore cause a change to the global variable as well. 

What is the value of <code>a</code> after this program finishes executing?

<pre>
def uppercase_string(s):
    s = s.upper()
    return s

a = ‘indeed'
b = uppercase_string(a)
</pre>

a. INDEED<br>
b. indeed <b># correct </b> <br> 
c. Indeed <br>
d. ERROR

Display after answer is revealed: Strings are immutable. As we have seem, a method applied to a string does not change the original string. Therefore, the function does not change the value of the original string.


<pre>
def add_to_list(l):
    m = l
    m.append(5)
    return m

a =  [1,2,3]
b = add_to_list(a)
</pre>

a. [1,2,3]<br>
b. [5,1,2,3] <br> 
c. [1,2,3,5]<b> # correct </b> <br>
d. ERROR


Should we have an open ended question? Explain why this worked as it did?

What is the value of <code>a</code> after this program finishes executing?

<pre>
def add_to_list(l):
    m = [1,2,3]
    m.extend(l)
    return m

a =  [1,2,3]
b = add_to_list(a)
</pre>

a. [1,2,3,1,2,3]<br>
b. [1,2,3] <b> # correct </b> <br> 
c. None of the above<br>
d. ERROR

Display after answer is revealed: In this example, a new list <code>m</code> is created inside the function. An operation is performed on <code>m</code>, not on the list <code>l</code>. Therefore, the function does not change list <code>l</code>, and list <code>a</code> also retains its original value.

## Any Unique Requirements or Notes?

---
# Technical Requirements
<em><strong></strong></em>

## Environment/s Used
Terminal. Python interpreter

## Language/s Used
<em></em>

## Package/s Required
<em>Python 3</em>

---
# Test Requirements
<em>This is the space to indicate what specifically about the student actions in the exercise needs to be tested. These specifications are the basis of how feedback or grading is given to the student. <strong>Don't worry about the specific method for verifying this initially, just focus on what needs to be checked from the student's actions to validate that they reached the key technical outcome for the exercise. Please also note that not all of these test types need to be specified, only what is necessary to test against the key outcome.</strong></em>

## Outcome Tests
<em>Indicate here criteria that should be tested relating to the outcomes or outputs of a student's actions in the exercise.</em>

## Student Code Tests
<em>This relates to specific aspects of the student's code which need to be assessed. The best way to indicate these requirements is with comments in your solution code file, indicating the parts of the code which need to be verified. This helps make the requirements less abstract. However, if you have any requirements that are better explained long form, please do so below.</em>

## Process Tests
<em>Indicate here criteria that should be tested relating to the process by which the student reached their outcomes in the exercise.</em>

---
#  Implementation Decisions

## Graded or Ungraded:
<em>This is easily adjusted in future iterations, but this is a place to indicate whether this exercise will pass a grade to the Canvas gradebook, just provide smart feedback to the student without a grade, or simply serve as a sandbox environment with no evaluation.</em>

## Exercise Type:
<em>This will always be determined in collaboration with the developers, designers, and authors based on the requirements above, what is most feasible and meets the key objectives.</em>

## Success Message
<em>This is the message the student will see when they complete the exercise, in the case that this is an exercise which provides automatic feedback. This should be written after the implementation decisions are made.</em>

## Test Case Failure Messages
<em>These should be written later in development, and only apply to automatically tested programming exercises. These will be written in accordance with the test cases developed for the exercise, which will also need to be specified here.</em>

## Environment Layout:
<em>This is how the environment components will be presented to students. This will usuall relate to Codio panes and what they contain.</em>

## Custom Codio Menu Items:
<em>This is a space to indicate any buttons that will need to be present in the Codio menu beyond the default items in the template.</em>

## New Integrations Required:
<em>We will indicate here if this exercise requires any new and unestablished integrations with Codio or Canvas.</em>
