#!/usr/bin/env python
# HW04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports
import random

# Body

def guessing(chance):
	guess = raw_input('Guess an integer between 1 and 25 inclusive: ')
	try:
		guess_int = int(guess)
		return guess_int
	except:
		if chance > 1: # to set text if the user still has guessing chances left.
			print "try again.. give a number this time"
			return "I went thru exception"
		else:	# last chance text
			print "sorry... that was your last guess and you entered a string. All your guesses were incorrect and you've run out of chances to guess"
			return "I went thru exception"
def check(random_num):
	chance = 5
	 # Remove this and replace with your function calls
	while chance > 0 : # while you still have one or some of your 5 chances
		guess_int = guessing(chance)
		chance -= 1
		if guess_int != "I went thru exception": # don't evaluate the expressions in the loop if the guess was a string
			if guess_int == random_num:
				print(" Congratulations! you guessed the right number")
				break
			elif guess_int > random_num:
				print "number too high"
			else:		
				print "number too low"
		else:
			continue
	if(chance == 0 and guess_int != "I went thru exception"): # ran out of guessing chances and the last guess was an integer
		print "All your guesses were incorrect and you've run out of chances to guess"



################################################################################
def main():
	random_num = random.randrange(1,25)
	print random_num
	check(random_num)

if __name__ == '__main__':
    main()