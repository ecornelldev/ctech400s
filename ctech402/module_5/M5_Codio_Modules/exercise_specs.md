# Exercise Title: Modules
---
# Instructional Requirements
## Key Technical Outcome

## Exercise Context

## Exercise Instructions

Updated:
Examine the code in <code>exercise.py</code>. It is using the <code>stats</code> module to find the mean, median, range and  standard deviation of a list of numbers.
However, while <code>stats.py</code> contains functions to find the mean, median and range, it does not contain a function to find the standard deviation.

The standard deviation of a group of numbers is a measure of how much the numbers are spread out around the mean.

To calculate the standard deviation of a list of numbers, do the following:

1. Compute the mean of the numbers.  
2. Subtract that mean from each number and square the result. You will have a new group of numbers.
3. Compute the mean of those numbers.
4. Find the square root of that mean.

Implement the <code>standard_deviation</code> function within <code>stats.py</code> so that <code>exercise.py</code> can successfully run.
(Note: Do not make changes to exercise.py)



**sum is not a good example. The students already know about sum() so the question is trivial. They also can get themselves into name conflicts quickly if they aren't careful because stats.sum and sum are easy to mix up. I would rather have them define and use some other function**

## Environment/s Used
Terminal. Python interpreter. Code editor.
** Pre-load starter code AND stats.py
** starter code is exercise.py and stats.py
