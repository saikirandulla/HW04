#!/usr/bin/env python
# HW04_ex08_11

# The following functions are all intended to check whether a string contains 
# any lowercase letters, but at least some of them are wrong. For each function, 
# describe what the function actually does (assuming that the parameter is a
# string).

# Do not merely paste the output as a counterexample into the documentation 
# string, explain what is wrong.

################################################################################
# Body

def any_lowercase1(s):
	"""Explain what is wrong, if anything, here.
	the control goes out the function after hitting the return statement the first time. This code returns
	boolean value True if the first letter in the string is of lowercase and False otherwise. It doesn't 
	proceed beyond the first character of the string
	"""
	for c in s:
		if c.islower():
			return True
		else:
			return False


def any_lowercase2(s):
    """Explain what is wrong, if anything, here.
	the control goes out the function after hitting the return statement the first time. This code returns
	the string 'True' if the first letter in the string is of lowercase and False otherwise. It doesn't 
	proceed beyond the first character of the string
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    """Explain what is wrong, if anything, here.
	This code returns true when the last character in the string is lowercase and false otherwise
    """
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    """Explain what is wrong, if anything, here.
	This function returns True even if there is a single lowercase letter in the string. will return false only if
	all the characters in the string are uppercase.	
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    """Explain what is wrong, if anything, here.
    """
    for c in s:
        if not c.islower():
            return False
    return True

################################################################################
def main():

    # Remove print("Hello World!") and for each function above that is wrong, 
    # call that function with a string for which the function returns
    # incorrectly
	print any_lowercase1("thisStringmessesupthefunction")
	print any_lowercase2("thisStringmessesupthefunction")
	print any_lowercase3("thisStringmessesupthefunction")
	print any_lowercase4("aaAAAAAAAAAA")
	print any_lowercase5("aaAa")

if __name__ == '__main__':
    main()