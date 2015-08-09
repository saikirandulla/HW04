#!/usr/bin/env python
# HW04_ex08_05

# The following program counts the number of times the letter a appears in a 
# string:

#     word = 'banana'
#     count = 0
#     for letter in word:
#         if letter == 'a':
#             count = count + 1
#     print count

# Encapsulate this code in a function named "count", and generalize it so that 
# it accepts the string and the letter as arguments.

################################################################################
# Imports


# Body

def count(word , let):
	count = 0
	for letter in word:
		if letter == let:
			count = count + 1
	print "Number of ", let + "'s in", word + " is", count
	


################################################################################
def main():
	count("Hello World!", "o") 
	count("aaaaaaaaaaaaaaa", "b")
	count("creative", "e")
	count("Golden Gate", "g")
	count("Golden Gate", "G")
if __name__ == '__main__':
    main()