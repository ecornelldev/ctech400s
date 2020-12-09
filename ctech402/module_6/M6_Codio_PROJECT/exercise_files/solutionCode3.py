####
# 
# Player and Computer each have 3 dice
# They each roll all 3 dice one time
# They are allowed to re-roll ONE die.
#
#######

import random

player_score = 0
computer_score = 0

# define roll function
# define roll function
def roll_three_dice():

	rolls = []
	for i in range(3):
		r = random.randint(1,6)
		print(str(r))
		rolls.append(r) #total = total + r
	
	return rolls
	
def do_they_match(dieArray):

	return all(x == dieArray[0] for x in dieArray)
	
		
def compute_total(list_of_values):

	total = 0
	for val in list_of_values:
		total = total + val
	
	return total

# Computer and user roll below:


while True:
	
	print("computer rolled:")
	comp_rolls = roll_three_dice()
	computer_score += compute_total(comp_rolls)
	
	if do_they_match(comp_rolls):
		print("Computer matches 3 dice! Scores extra 5 points!")
		computer_score += 5
		break
		
	
	print("You rolled:")
	player_rolls = roll_three_dice()
	player_score += compute_total(player_rolls)
	
	if do_they_match(player_rolls):
		print("You match 3 dice! You score an extra 5 points!")
		player_score += 5
		break	
	

print("Computer's total score: " + str(computer_score))
print("You're total score: " + str(player_score))


# print final score and report who wins below:

if computer_score > player_score:
	print("COMPUTER WINS :(" )
elif player_score > computer_score:
	print("YOU WIN!!! :) " )
else:
	print("TIED!")