# Exercise Title:
---
# Instructional Requirements
## Key Technical Outcome
## Exercise Context
Multiple choice and TF questions

## Exercise Instructions

 Choose the result of the following expressions:
 
 1. <pre>['one', 'two'] + ['three', 'four'] + [] + ['one']</pre>

['one', 'two', 'three', 'four', '', 'one'] <br>
#<b> correct: </b><br>
['one', 'two', 'three', 'four', 'one']<br> 
['one', 'two', 'three', 'four']<br>


2. <pre>['square', 'circle'] * 3</pre>

['square', 'square', 'square', 'circle'] <br>
['square', 'circle', 'circle', 'circle']<br>
#<b>correct: </b><br>
['square', 'circle', 'square', 'circle', 'square', 'circle']  <br>


3. <pre>['red', 'blue'] + ['orange'] * 3 </pre>
 
['red', 'blue', 'orange', 'red', 'blue', 'orange', 'red', 'blue', 'orange'] <br>
#<b>correct:</b><br>
['red', 'blue', 'orange', 'orange', 'orange'] <br>
[''red', 'blue', 'red', 'blue', 'red', 'blue', 'orange'] <br>
 
 
 Do the following expressions evaluate to True or False?:
 
 #<b>False: </b>
 
 1. <pre> ['dog', 'cat', 'mouse' , 'rabbit'] == ['dog' , 'cat', 'rabbit', 'mouse'] </pre>   
 
 #<b>True:</b>
 
 2. <pre> [10, 45, 15, 5] > [10, 30, 20, 6] </pre>
  #<b>False:</b>
  
 3. <pre>array_one = ['orange', 5, 6, 'green']
    array_two = ['green', 5, 6, 'orange']
    array_one == array_two </pre>

 
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
