# Exercise Title: Dictionary Basics
---
## Key Technical Outcome

## Exercise Context
Syntax, making, looking up elements, assignment

## Exercise Instructions

Q1: Below is a dictionary that contains a simple itinerary with one main task or appointment to do per day.

<code>weekly_planner = { 'Monday': 'hair appointment'  , 'Tuesday': 'pick up groceries', 'Wednesday': 'baseball practice'}</code>

How do you access Monday's itinerary?

a. weekly_planner[1] <br>
b. weekly_planner['hair appointment'] <br>
c. weekly_planner[0] <br>
d. weekly_planner['Monday'] <b># correct </b>

Q2: Below is a dictionary that contains a simple itinerary with one main task or appointment to do per day.

<code>weekly_planner = { 'Monday': 'hair appointment'  , 'Tuesday': 'pick up groceries', 'Wednesday': 'baseball practice'}</code> 

What is the value of the expression `weekly_planner[2]`?

a. 'Tuesday' <br>
b. error <b># correct </b> # perhaps give explanation again as to why this is a problem<br>  
c. 'Wednesday' <br>
d. 'baseball practice' <br>

Display when answer is revealed:  Dictionaries use keys instead of integer indices to look up values. <code>weekly_planner </code> does not contain a key of 2 and so <code> weekly_planner[2]</code> will result in an error,

Q3: You would like to have dinner with friends on Friday. Your entry will be 'dinner with friends.' How would you create a new key/value pair in the weekly_planner dictionary? <br>
<b>(free text, answer is weekly_planner['Friday'] = 'dinner with friends')</b>

Q4: Examine the dictionary and list below. Which of the following operations result in an error (select all that apply):

<pre>d = {45:2, 'x': 12, 'Frank': 'f345P', 'cat': 'not dog'}<br>
l = ['cat', 'Frank', 67]</pre>

d[45] <br>
d[0] <b> # error </b><br>
d['Frank'] = 15 <br>
l['Frank'] <b> # error </b><br>
x = d['not dog']<b> # error </b><br>
d['pizza'] = 'mushrooms' <br>
l[2] = 3 <br>
