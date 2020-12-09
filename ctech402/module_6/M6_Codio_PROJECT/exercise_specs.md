# Exercise Title:
---
# Instructional Requirements
## Key Technical Outcome
Yahtzee-like game: user vs computer

## Interpretive Option:
<b>Exercise Context</b>
For this final course project, you will create a game similar to the card game professor Grimmelmann created in this module. Instead of cards, you will write a program in which you roll and reroll three or more dice to try to score higher values than the computer.

**Suggestions:
* Have player and computer take turns rerolling until one of them has three matching dice. This effectively forces them to use a loop.
* Add a reusable function for checking whether a player has three matching dice.
* Score is the total of your dice, but the player who matched three first gets a 5-point bonus?
* Provide a sample transcript showing how a few plays of the game should look? This will help students a lot in understanding what they need to do.**

# UPDATED INSTRUCTIONS:

For this final course project, you will create a game similar to the card game professor Grimmelmann created in this module. Instead of cards, you will be playing with dice. Write a program in which you and the computer roll and re-roll three dice to compete for the highest score.

1. You and the computer should take turns rolling three dice, with possible values of 1-6.
2. After each roll, save both the computer and user's score
3. The game ends when one player rolls three matching dice (For example, one player rolls three dice each having the value of 4).
4. Give a 5 point bonus to the player who rolled the three matching dice to end the game.
5. Tally up the score at the end of the game. The player with the highest score wins. Display the final score and the winner.

Your program should contain one re-usable function that checks whether a player has three matching dice and returns the boolean result.

To generate a die roll, you should use the <code>random.randint()</code> function to generate a random integer value between 1 and 6 

Below is a sample transcript?? of one game:

<pre>
Computer rolled:
6
4
1
You rolled:
3
5
6
Computer rolled:
5
3
1
You rolled:
4
2
6
Computer rolled:
3
3
5
You rolled:
2
2
2
You match 3 dice! You score an extra 5 points!
Computer's total score: 31
You're total score: 32
YOU WIN!!! 
</pre>


# END INSTRUCTIONS


<b>Exercise Instructions</b>
To successfully complete this task, your program must include each of the following:
  1. Printed statements that clearly narrate the events of the game to the conclusion.
  2. A reusable function for rolling (and rerolling) the dice (with possible values 1-6), implemented for both the player and and computer.
  3. The opportunity for strategy: Both the computer and player should have a chance to reroll at least one die value of their selection
  4. Once all rolls are complete, whoever had the highest total score OR 3 matching die rolls wins.
  5. Comment the sections of your code explaining your development process and the rules/events that depict the narrative of the game.
  6. Your code must include at least one for or while loop.

To complete this project, you will need to utilize the <code>random</code> module package that contains the function <code>randint</code> that will help you create your dice rolling feature. Use the randint function to generate a random integer value between 1-6.

We will include some basic initial code and variables to get you started. You may modify or rename these variables for your own style or purposes.


## <b>Instructed Options:</b>
<b>Idea #1:</b>

It's time to create your own game.<br>
Make a simple dice game where a user and a computer each roll 5 dice and compete to get the highest score.<br>
Create the option for the user to re-roll one die:<br>
After the computer and user roll all 5 dice, display both the user's and computer's (hand?) to the user.
Ask the user if s/he wishes to re-roll one die.  <br>
If the user would like to re-roll, prompt the user to specify which die to roll. <br>
Both user and computer should re-roll. <br>
Tally up the score.<br>
The highest score at the end wins.<br>
Display the final score and who wins. <br>

Hint: To generate a die roll, you should use the <code>random.randint()</code> function to generate a random integer value between 1 and 6 

Additional functionality: Make the game more interesting by adding additional rounds. In other words, the user and computer can each role 5 dice multiple times, and the final score will take into account all rounds.

<b>Idea #2</b>
It's time to create your own game.<br>
Make a simple dice game where a user and a computer each roll 5 dice compete to get the highest score.<br>
The game should have three rounds: the user and computer both roll 5 dices THREE times. <br>
Create the option for the user to re-roll:<br>
After each round, the user has the option to re-roll his/her dice for a different score.
Ask the user if s/he wishes to re-roll  <br>
If the user would like to re-roll, both user and computer should re-roll all 5 dice. <br>
Tally up the score from all rounds.<br>
The highest score at the end wins.<br>
Display the final score and who wins. <br>

Hint: To generate a die roll, you should use the <code>random.randint()</code> function to generate a random integer value between 1 and 6 

Additional functionality: Make the game more interesting by allowing the user to input how many rounds he/she would like to play at the beginning of the game.


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
